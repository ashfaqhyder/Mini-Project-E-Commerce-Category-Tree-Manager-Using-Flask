# E-Commerce Category Tree Manager

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-0f766e?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-134e4a?style=for-the-badge&logo=flask&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-14b8a6?style=for-the-badge&logo=json&logoColor=white)
![Status](https://img.shields.io/badge/Project-Working-0d9488?style=for-the-badge)

<h3>A Flask mini app for managing hierarchical e-commerce categories using a tree data structure.</h3>

<p>
  <img src="https://readme-typing-svg.demolab.com?font=Segoe+UI&weight=600&size=22&duration=2600&pause=700&color=0F766E&center=true&vCenter=true&width=900&lines=Tree-Based+Category+Management+System;Preorder+%7C+Inorder+%7C+Postorder+Traversal;Search%2C+Add%2C+Rename%2C+Delete+Categories;Flask+Frontend+%2B+Backend+API+%2B+JSON+Storage" alt="Typing animation" />
</p>

</div>

---

## Overview

This project models an e-commerce platform's category structure as a **tree**.  
Each category is a node, and each subcategory is stored as a child node.

Example:

```text
All Products
├── Electronics
│   ├── Laptops
│   │   ├── Gaming Laptops
│   │   └── Business Laptops
│   └── Mobiles
│       ├── Android Phones
│       └── iPhones
└── Fashion
    ├── Men
    │   ├── Shirts
    │   └── Shoes
    └── Women
        ├── Dresses
        └── Handbags
```
The app provides a clean GUI for category management, supports traversal operations, and stores data persistently using JSON.

Features
Visual hierarchical category display
Add a new category or subcategory
Rename an existing category
Delete a category
Search for a category and display its full path
Preorder traversal
Inorder traversal
Postorder traversal
JSON-based storage for persistent data
Clean teal-themed UI inspired by modern dashboard layouts
Why Tree Data Structure?
An e-commerce category system is naturally hierarchical:

All Products is the root
main categories like Electronics and Fashion are child nodes
subcategories like Laptops and Gaming Laptops form deeper branches
This makes the tree the most appropriate data structure for representing product categories.

Traversal Algorithms
1. Preorder Traversal
Visit current node -> visit child nodes

Example:

All Products -> Electronics -> Laptops -> Gaming Laptops -> Business Laptops -> Mobiles -> Android Phones -> iPhones -> Fashion -> Men -> Shirts -> Shoes -> Women -> Dresses -> Handbags
2. Inorder Traversal
For this project, inorder is adapted for a general tree by visiting:

first half of children
current node
remaining children
This is included for comparison, although inorder is more naturally suited to binary trees.

3. Postorder Traversal
Visit child nodes -> visit current node

Example:

Gaming Laptops -> Business Laptops -> Laptops -> Android Phones -> iPhones -> Mobiles -> Electronics -> Shirts -> Shoes -> Men -> Dresses -> Handbags -> Women -> Fashion -> All Products
Best Traversal for Hierarchical Display
Preorder traversal is the most suitable for displaying product categories hierarchically.
Reason:
it visits the parent category first
then it visits the subcategories under that parent
this matches how real e-commerce websites show navigation menus
Example:

Electronics
  Laptops
    Gaming Laptops
This is how users expect categories to appear when browsing products.

In contrast:

Inorder is mainly useful for binary trees
Postorder shows child categories before the parent, which is not ideal for visual hierarchy display
Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Flask
Storage: JSON
Language: Python
Project Structure:
```text
ecommerce-category-tree/
│
├── app.py
├── tree.py
├── storage.py
├── requirements.txt
├── README.md
│
├── data/
│   └── categories.json
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── app.js
```
API Endpoints
Method	Endpoint	Description
```text
GET	/	Load the main UI
GET	/api/categories	Get the full category tree
GET	/api/traversal/preorder	Get preorder traversal
GET	/api/traversal/inorder	Get inorder traversal
GET	/api/traversal/postorder	Get postorder traversal
GET	/api/search?q=CategoryName	Search for a category
POST	/api/categories	Add a category
PUT	/api/categories	Rename a category
DELETE	/api/categories	Delete a category
```
Installation and Run
1. Clone the repository 
git clone https://github.com/your-username/ecommerce-category-tree.git
cd ecommerce-category-tree
2. Create a virtual environment
   python -m venv venv
3. Activate the virtual environment
    Windows
    
    venv\Scripts\activate
    Mac/Linux
    
    source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Run the application
python app.py

6. Open in browser
http://127.0.0.1:5000



Screenshots:
<img width="1917" height="938" alt="image" src="https://github.com/user-attachments/assets/43f5c9da-598a-4b0f-8370-b80fb1152135" />


Explanation
This project uses a tree data structure to represent the hierarchical organization of e-commerce categories.
Each node represents a category, and child nodes represent subcategories.
The system implements preorder, inorder, and postorder traversal algorithms.
Among them, preorder traversal is the most suitable for displaying categories because it visits the parent before its children, matching the natural structure of online product navigation.

Future Improvements
SQLite database integration
User authentication for admin access
Expand/collapse tree controls
Product mapping inside categories
Dark mode UI

Author:

Ashfaq Hyder C S


<div align="center"> <sub>Built with Flask, trees, and a pleasantly orderly amount of recursion.</sub> </div> 
<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-0f766e?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-134e4a?style=for-the-badge&logo=flask&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-14b8a6?style=for-the-badge&logo=json&logoColor=white)
![Tree](https://img.shields.io/badge/Data%20Structure-Tree-0d9488?style=for-the-badge)
![Traversal](https://img.shields.io/badge/Traversal-Preorder%20%7C%20Inorder%20%7C%20Postorder-115e59?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-0f766e?style=for-the-badge)

</div>

