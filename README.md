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

## Deploy to Render

This project now includes:

- `render.yaml` for Render Blueprint deployment
- `Procfile` with a production start command
- `.python-version` to keep Python consistent
- `/health` endpoint for Render health checks
- `DATA_FILE` support so the JSON storage path can be changed by environment variable

### Option A: Deploy with `render.yaml` (recommended)

1. Push this project to GitHub.
2. Sign in to Render and connect your GitHub account.
3. In Render, click `New` -> `Blueprint`.
4. Select your repository.
5. Render will detect `render.yaml`.
6. Review the generated service settings:
   - Runtime: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Health Check Path: `/health`
7. Click `Apply`.
8. Wait for the first deploy to finish.
9. Open the generated `onrender.com` URL.

### Option B: Deploy as a Web Service manually

1. Push the project to GitHub.
2. In Render, click `New` -> `Web Service`.
3. Connect your repository.
4. Use these settings:
   - Language: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Add environment variables if needed:
   - `PYTHON_VERSION=3.12.10`
   - `DATA_FILE=data/categories.json`
6. Create the service and wait for the deploy to complete.

### Important storage note

This app stores category data in `data/categories.json`.

Render's documentation says web services use an ephemeral filesystem by default, which means file changes are lost after a restart or redeploy. Render also documents that a persistent disk can preserve files, but only under the disk's mount path. Persistent disks are available only on paid Render web services.

If you want category changes to persist on Render, use one of these:

1. Attach a persistent disk and move the data file under the mount path.
2. Replace JSON storage with a database such as PostgreSQL or SQLite on persistent storage.

### How to use a persistent disk on Render

If you attach a persistent disk in Render:

1. Open your Render web service.
2. Go to the disk settings for the service.
3. Add a disk and choose a mount path.
4. Use a mount path under your app directory, such as:
   - `/opt/render/project/src/data`
5. Update the `DATA_FILE` environment variable to:
   - `/opt/render/project/src/data/categories.json`
6. Redeploy the service.

That makes category changes survive future restarts and redeploys.

### After deployment

- Every push to the connected branch can auto-deploy on Render.
- You can watch deploy logs from the Render dashboard.
- The app health check is available at `/health`.

### Useful commands

Local development:

`python app.py`

Production-style local run:

`gunicorn app:app --bind 0.0.0.0:5000`
