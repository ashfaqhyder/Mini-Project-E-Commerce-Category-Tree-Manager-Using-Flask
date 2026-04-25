from flask import Flask, jsonify, render_template, request

from storage import CategoryStorage
from tree import CategoryNode, CategoryTree


app = Flask(__name__)
storage = CategoryStorage("data/categories.json")


def load_tree() -> CategoryTree:
    return storage.load_tree()


def save_tree(tree: CategoryTree) -> None:
    storage.save_tree(tree)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/categories")
def get_categories():
    tree = load_tree()
    return jsonify(tree.to_dict())


@app.get("/api/traversal/<order_name>")
def get_traversal(order_name: str):
    tree = load_tree()

    if order_name == "preorder":
        result = tree.preorder()
    elif order_name == "inorder":
        result = tree.inorder()
    elif order_name == "postorder":
        result = tree.postorder()
    else:
        return jsonify({"error": "Unsupported traversal type."}), 400

    return jsonify(
        {
            "traversal": order_name,
            "result": result,
            "recommended_for_display": order_name == "preorder",
        }
    )


@app.get("/api/search")
def search_category():
    query = request.args.get("q", "").strip()
    parent_name = request.args.get("parent_name", "").strip()
    if not query:
        return jsonify({"error": "Query is required."}), 400

    tree = load_tree()
    try:
        match = tree.find(query, parent_name or None)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    if not match:
        return jsonify({"found": False, "message": "Category not found."}), 404

    return jsonify({"found": True, "category": match})


@app.post("/api/categories")
def add_category():
    payload = request.get_json(silent=True) or {}
    name = str(payload.get("name", "")).strip()
    parent_name = str(payload.get("parent_name", "")).strip()

    if not name:
        return jsonify({"error": "Category name is required."}), 400

    tree = load_tree()
    try:
        if parent_name:
            tree.add_category(name, parent_name)
        else:
            tree.root.add_child(CategoryNode(name))
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    save_tree(tree)
    return jsonify({"message": "Category added successfully.", "tree": tree.to_dict()}), 201


@app.put("/api/categories")
def rename_category():
    payload = request.get_json(silent=True) or {}
    current_name = str(payload.get("current_name", "")).strip()
    new_name = str(payload.get("new_name", "")).strip()
    parent_name = str(payload.get("parent_name", "")).strip()

    if not current_name or not new_name:
        return jsonify({"error": "Current and new names are required."}), 400

    tree = load_tree()
    try:
        tree.rename_category(current_name, new_name, parent_name or None)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    save_tree(tree)
    return jsonify({"message": "Category renamed successfully.", "tree": tree.to_dict()})


@app.delete("/api/categories")
def delete_category():
    payload = request.get_json(silent=True) or {}
    name = str(payload.get("name", "")).strip()
    parent_name = str(payload.get("parent_name", "")).strip()

    if not name:
        return jsonify({"error": "Category name is required."}), 400

    tree = load_tree()
    try:
        tree.delete_category(name, parent_name or None)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    save_tree(tree)
    return jsonify({"message": "Category deleted successfully.", "tree": tree.to_dict()})


if __name__ == "__main__":
    app.run(debug=True)
