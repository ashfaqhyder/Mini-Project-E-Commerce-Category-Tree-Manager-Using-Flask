# E-Commerce Category Tree Manager

This Flask mini app demonstrates how an e-commerce platform can organize categories using a tree data structure. Each category is a node, and subcategories are stored as child nodes.

## Features

- Visual category hierarchy
- Add, rename, and delete categories
- Search categories and show their path
- Preorder, inorder, and postorder traversals
- JSON-based storage

## Why Preorder Is Best for Display

Preorder traversal visits the current category before its subcategories:

`Parent -> Child -> Subchild`

That mirrors how online shopping sites display nested menus. Inorder is mainly suited to binary trees, while postorder is more useful when child nodes must be processed before the parent.

## Run the Project

1. Create a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Start the app with `python app.py`.
4. Open `http://127.0.0.1:5000`.
