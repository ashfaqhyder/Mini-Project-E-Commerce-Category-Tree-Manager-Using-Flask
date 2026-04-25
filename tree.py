from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CategoryNode:
    name: str
    children: list["CategoryNode"] = field(default_factory=list)

    def add_child(self, child: "CategoryNode") -> None:
        if any(existing.name.lower() == child.name.lower() for existing in self.children):
            raise ValueError(f"'{child.name}' already exists under '{self.name}'.")
        self.children.append(child)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "children": [child.to_dict() for child in self.children],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CategoryNode":
        return cls(
            name=data["name"],
            children=[cls.from_dict(child) for child in data.get("children", [])],
        )


class CategoryTree:
    def __init__(self, root: CategoryNode):
        self.root = root

    def to_dict(self) -> dict:
        return self.root.to_dict()

    def _normalize(self, value: str) -> str:
        return value.strip().lower()

    def find_node(self, name: str, node: CategoryNode | None = None) -> CategoryNode | None:
        current = node or self.root
        if current.name.lower() == self._normalize(name):
            return current

        for child in current.children:
            match = self.find_node(name, child)
            if match:
                return match
        return None

    def _find_matches(
        self,
        name: str,
        node: CategoryNode,
        path: list[str],
        matches: list[dict],
    ) -> None:
        current_path = [*path, node.name]
        if node.name.lower() == self._normalize(name):
            matches.append({"name": node.name, "path": current_path})

        for child in node.children:
            self._find_matches(name, child, current_path, matches)

    def _search_root(self, parent_name: str | None) -> tuple[CategoryNode, list[str]]:
        if not parent_name:
            return self.root, [self.root.name]

        if self.root.name.lower() == self._normalize(parent_name):
            return self.root, [self.root.name]

        matches: list[dict] = []
        self._find_matches(parent_name, self.root, [], matches)

        if not matches:
            raise ValueError(f"Parent node '{parent_name}' not found.")

        if len(matches) > 1:
            raise ValueError(
                f"Parent node '{parent_name}' is ambiguous. "
                "Please choose a more specific parent node."
            )

        target_path = matches[0]["path"]
        node = self.find_node_by_path(target_path)
        if not node:
            raise ValueError(f"Parent node '{parent_name}' not found.")
        return node, target_path

    def find_node_by_path(self, path: list[str]) -> CategoryNode | None:
        if not path or path[0].lower() != self.root.name.lower():
            return None

        current = self.root
        for segment in path[1:]:
            next_node = None
            for child in current.children:
                if child.name.lower() == segment.lower():
                    next_node = child
                    break
            if not next_node:
                return None
            current = next_node
        return current

    def find(self, name: str, parent_name: str | None = None) -> dict | None:
        search_root, root_path = self._search_root(parent_name)
        matches: list[dict] = []
        self._find_matches(name, search_root, root_path[:-1], matches)

        if not matches:
            return None

        if len(matches) > 1:
            raise ValueError(
                f"Multiple categories named '{name}' were found. "
                "Provide a parent node to narrow the search."
            )

        return matches[0]

    def add_category(self, name: str, parent_name: str) -> None:
        parent = self.find_node(parent_name)
        if not parent:
            raise ValueError(f"Parent category '{parent_name}' not found.")
        parent.add_child(CategoryNode(name))

    def rename_category(
        self,
        current_name: str,
        new_name: str,
        parent_name: str | None = None,
    ) -> None:
        if self.root.name.lower() == self._normalize(current_name):
            self.root.name = new_name
            return

        search_root, root_path = self._search_root(parent_name)
        matches: list[dict] = []
        self._find_matches(current_name, search_root, root_path[:-1], matches)

        if not matches:
            raise ValueError(f"Category '{current_name}' not found.")

        if len(matches) > 1:
            raise ValueError(
                f"Multiple categories named '{current_name}' were found. "
                "Provide a parent node to rename the correct one."
            )

        node = self.find_node_by_path(matches[0]["path"])
        if not node:
            raise ValueError(f"Category '{current_name}' not found.")
        node.name = new_name

    def delete_category(self, name: str, parent_name: str | None = None) -> None:
        if self.root.name.lower() == self._normalize(name):
            raise ValueError("The root category cannot be deleted.")

        search_root, root_path = self._search_root(parent_name)
        matches: list[dict] = []
        self._find_matches(name, search_root, root_path[:-1], matches)

        if not matches:
            raise ValueError(f"Category '{name}' not found.")

        if len(matches) > 1:
            raise ValueError(
                f"Multiple categories named '{name}' were found. "
                "Provide a parent node to delete the correct one."
            )

        target_path = matches[0]["path"]
        parent_path = target_path[:-1]
        parent = self.find_node_by_path(parent_path)

        if not parent:
            raise ValueError(f"Category '{name}' not found.")

        for index, child in enumerate(parent.children):
            if child.name.lower() == self._normalize(name):
                del parent.children[index]
                return

        raise ValueError(f"Category '{name}' not found.")

    def preorder(self) -> list[str]:
        result: list[str] = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: CategoryNode, result: list[str]) -> None:
        result.append(node.name)
        for child in node.children:
            self._preorder(child, result)

    def inorder(self) -> list[str]:
        result: list[str] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: CategoryNode, result: list[str]) -> None:
        midpoint = len(node.children) // 2
        for child in node.children[:midpoint]:
            self._inorder(child, result)
        result.append(node.name)
        for child in node.children[midpoint:]:
            self._inorder(child, result)

    def postorder(self) -> list[str]:
        result: list[str] = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: CategoryNode, result: list[str]) -> None:
        for child in node.children:
            self._postorder(child, result)
        result.append(node.name)
