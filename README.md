# E-Commerce Category Tree Manager

<p align="center">
  <img src="https://img.shields.io/badge/Flask-3.1.0-0F766E?style=for-the-badge&logo=flask&logoColor=white" alt="Flask badge">
  <img src="https://img.shields.io/badge/Python-Tree%20Data%20Structure-0F766E?style=for-the-badge&logo=python&logoColor=white" alt="Python badge">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-0F766E?style=for-the-badge" alt="Frontend badge">
  <img src="https://img.shields.io/badge/Status-Localhost%20Ready-0F766E?style=for-the-badge" alt="Status badge">
</p>

<p align="center">
  A visually interactive Flask application that models e-commerce categories using a tree data structure.
  Add, search, rename, delete, and traverse category nodes from one clean dashboard.
</p>

---

## Live Preview

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Segoe+UI&weight=700&size=24&pause=1000&color=0F766E&center=true&vCenter=true&width=900&lines=Manage+product+categories+with+a+tree+structure;Visualize+hierarchy+with+preorder%2C+inorder%2C+and+postorder;Search%2C+rename%2C+and+delete+duplicate+node+names+safely" alt="Typing animation">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Theme-Teal%20Dashboard%20UI-CCFBF1?style=flat-square&labelColor=0F766E&color=CCFBF1" alt="Theme badge">
  <img src="https://img.shields.io/badge/Traversal-Preorder%20Recommended-CCFBF1?style=flat-square&labelColor=0F766E&color=CCFBF1" alt="Traversal badge">
  <img src="https://img.shields.io/badge/Data-JSON%20Tree%20Storage-CCFBF1?style=flat-square&labelColor=0F766E&color=CCFBF1" alt="Data badge">
</p>

## Screenshots

Add your screenshots below after running the project locally.

### Home Screen

![Home Screen](./screenshots/home.png)

### Category Search

![Category Search](./screenshots/search.png)

### Traversal Output

![Traversal Output](./screenshots/traversal.png)

### Demo GIF

![Demo GIF](./screenshots/demo.gif)

Note:
If you do not have screenshots yet, keep this section as-is and add the files later inside a `screenshots/` folder.

## Features

- Visual category hierarchy rendered from a tree structure
- Add new categories under any parent node
- Rename categories with optional parent-node disambiguation
- Delete categories safely with optional parent-node disambiguation
- Search for a category and display its full path
- Highlight the exact matched node in the hierarchy
- Compare preorder, inorder, and postorder traversals
- Internal CSS styling inside the HTML template
- Local JSON-based storage for category data

## Tech Stack

- Python
- Flask
- HTML
- Internal CSS
- JavaScript
- JSON file storage

## Project Structure

```text
E-Commerce/
├── app.py
├── tree.py
├── storage.py
├── requirements.txt
├── README.md
├── data/
│   └── categories.json
├── static/
│   └── app.js
└── templates/
    └── index.html
```

## How It Works

Each category is stored as a node in a tree.

- A parent category can contain multiple child categories.
- Subcategories are stored in the `children` list.
- Traversal algorithms are used to explore the hierarchy in different orders.

Example:

```text
All Products
├── Electronics
│   ├── Laptops
│   │   ├── Gaming Laptops
│   │   └── Business Laptops
│   └── Mobiles
└── Fashion
    ├── Men
    └── Women
```

## Traversals

### Preorder

Visits:

```text
Parent -> Children
```

Why it is best for display:
Preorder shows the parent category before its subcategories, which matches how e-commerce menus are usually presented.

### Inorder

Inorder is more natural for binary trees. In this project, it is adapted for a general tree by visiting part of the children, then the node, then the remaining children.

### Postorder

Visits:

```text
Children -> Parent
```

Useful when child nodes must be processed before the parent, but not ideal for category navigation.

## Duplicate Node Handling

If two nodes have the same name, the application can use an optional `parent node` field while searching, renaming, or deleting.

Example:

- Search `Sandals` under parent node `Men`
- Search `Sandals` under parent node `Women`

This prevents the app from selecting the wrong node when duplicate names exist in different branches.

## Run Locally

### 1. Clone the project

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000
```

## Future Improvements

- Replace JSON storage with SQLite or PostgreSQL
- Add expand/collapse controls for large trees
- Add node-level edit buttons directly in the hierarchy
- Support drag-and-drop category reordering
- Add category descriptions and product counts

## Author Notes

This project is designed for local presentation and demonstration.
It focuses on tree-based category management, traversal visualization, and duplicate-node handling in a practical e-commerce scenario.
