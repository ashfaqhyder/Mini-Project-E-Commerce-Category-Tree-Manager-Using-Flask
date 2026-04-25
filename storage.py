import json
from pathlib import Path

from tree import CategoryNode, CategoryTree


class CategoryStorage:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.save_tree(self._default_tree())

    def load_tree(self) -> CategoryTree:
        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return CategoryTree(CategoryNode.from_dict(data))

    def save_tree(self, tree: CategoryTree) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(tree.to_dict(), file, indent=2)

    def _default_tree(self) -> CategoryTree:
        return CategoryTree(
            CategoryNode(
                "All Products",
                [
                    CategoryNode(
                        "Electronics",
                        [
                            CategoryNode(
                                "Laptops",
                                [
                                    CategoryNode("Gaming Laptops"),
                                    CategoryNode("Business Laptops"),
                                ],
                            ),
                            CategoryNode(
                                "Mobiles",
                                [
                                    CategoryNode("Android Phones"),
                                    CategoryNode("iPhones"),
                                ],
                            ),
                        ],
                    ),
                    CategoryNode(
                        "Fashion",
                        [
                            CategoryNode(
                                "Men",
                                [
                                    CategoryNode("Shirts"),
                                    CategoryNode("Shoes"),
                                ],
                            ),
                            CategoryNode(
                                "Women",
                                [
                                    CategoryNode("Dresses"),
                                    CategoryNode("Handbags"),
                                ],
                            ),
                        ],
                    ),
                ],
            )
        )
