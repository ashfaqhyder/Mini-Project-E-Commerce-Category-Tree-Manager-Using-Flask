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

    def find_node(self, name: str, node: CategoryNode | None = None) -> CategoryNode | None:
        current = node or self.root
        if current.name.lower() == name.lower():
            return current

        for child in current.children:
            match = self.find_node(name, child)
            if match:
                return match
        return None

    def find(self, name: str) -> dict | None:
        path: list[str] = []
        if self._find_with_path(name, self.root, path):
            return {"name": path[-1], "path": path}
        return None

    def _find_with_path(self, name: str, node: CategoryNode, path: list[str]) -> bool:
        path.append(node.name)
        if node.name.lower() == name.lower():
            return True

        for child in node.children:
            if self._find_with_path(name, child, path):
                return True

        path.pop()
        return False

    def add_category(self, name: str, parent_name: str) -> None:
        parent = self.find_node(parent_name)
        if not parent:
            raise ValueError(f"Parent category '{parent_name}' not found.")
        parent.add_child(CategoryNode(name))

    def rename_category(self, current_name: str, new_name: str) -> None:
        if self.root.name.lower() == current_name.lower():
            self.root.name = new_name
            return

        node = self.find_node(current_name)
        if not node:
            raise ValueError(f"Category '{current_name}' not found.")
        node.name = new_name

    def delete_category(self, name: str) -> None:
        if self.root.name.lower() == name.lower():
            raise ValueError("The root category cannot be deleted.")

        if not self._delete_from_parent(self.root, name):
            raise ValueError(f"Category '{name}' not found.")

    def _delete_from_parent(self, parent: CategoryNode, name: str) -> bool:
        for index, child in enumerate(parent.children):
            if child.name.lower() == name.lower():
                del parent.children[index]
                return True
            if self._delete_from_parent(child, name):
                return True
        return False

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
