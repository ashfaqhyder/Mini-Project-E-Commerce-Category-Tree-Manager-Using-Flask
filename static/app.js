const treeContainer = document.getElementById("treeContainer");
const traversalOutput = document.getElementById("traversalOutput");
const statusMessage = document.getElementById("statusMessage");
const searchResult = document.getElementById("searchResult");

let highlightedPath = null;

async function fetchJson(url, options = {}) {
  const response = await fetch(url, options);
  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.error || data.message || "Something went wrong.");
  }

  return data;
}

function renderTree(node, path = []) {
  const wrapper = document.createElement("div");
  wrapper.className = "tree-node";

  const label = document.createElement("div");
  label.className = "node-label";
  label.textContent = node.name;
  const currentPath = [...path, node.name];

  if (
    highlightedPath &&
    highlightedPath.length === currentPath.length &&
    highlightedPath.every((segment, index) => segment === currentPath[index])
  ) {
    label.classList.add("match");
  }

  wrapper.appendChild(label);

  if (node.children && node.children.length) {
    const childrenWrapper = document.createElement("div");
    childrenWrapper.className = "children";
    node.children.forEach((child) => {
      childrenWrapper.appendChild(renderTree(child, currentPath));
    });
    wrapper.appendChild(childrenWrapper);
  }

  return wrapper;
}

async function loadTree() {
  const tree = await fetchJson("/api/categories");
  treeContainer.innerHTML = "";
  treeContainer.appendChild(renderTree(tree));
}

async function runTraversal(order) {
  const data = await fetchJson(`/api/traversal/${order}`);
  traversalOutput.textContent = `${order.toUpperCase()}:\n${data.result.join(" -> ")}`;
  statusMessage.textContent = `${order} traversal loaded successfully.`;
}

async function handleFormSubmit(event, method, url, bodyBuilder) {
  event.preventDefault();

  try {
    const body = bodyBuilder(new FormData(event.target));
    const data = await fetchJson(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    highlightedPath = null;
    await loadTree();
    statusMessage.textContent = data.message;
    searchResult.textContent = "No search performed yet.";
    event.target.reset();
  } catch (error) {
    statusMessage.textContent = error.message;
  }
}

document.getElementById("addForm").addEventListener("submit", (event) =>
  handleFormSubmit(event, "POST", "/api/categories", (formData) => ({
    name: formData.get("name"),
    parent_name: formData.get("parent_name"),
  }))
);

document.getElementById("renameForm").addEventListener("submit", (event) =>
  handleFormSubmit(event, "PUT", "/api/categories", (formData) => ({
    current_name: formData.get("current_name"),
    new_name: formData.get("new_name"),
    parent_name: formData.get("parent_name"),
  }))
);

document.getElementById("deleteForm").addEventListener("submit", (event) =>
  handleFormSubmit(event, "DELETE", "/api/categories", (formData) => ({
    name: formData.get("name"),
    parent_name: formData.get("parent_name"),
  }))
);

document.getElementById("searchForm").addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);
  const query = String(formData.get("query") || "").trim();
  const parentName = String(formData.get("parent_name") || "").trim();

  if (!query) {
    statusMessage.textContent = "Please enter a category name to search.";
    return;
  }

  try {
    const params = new URLSearchParams({ q: query });
    if (parentName) {
      params.set("parent_name", parentName);
    }

    const data = await fetchJson(`/api/search?${params.toString()}`);
    highlightedPath = data.category.path;
    await loadTree();
    searchResult.textContent = `Found: ${data.category.path.join(" -> ")}`;
    statusMessage.textContent = "Search completed successfully.";
  } catch (error) {
    highlightedPath = null;
    await loadTree();
    searchResult.textContent = error.message;
    statusMessage.textContent = "Search completed with no match.";
  }
});

document.querySelectorAll("[data-traversal]").forEach((button) => {
  button.addEventListener("click", () => runTraversal(button.dataset.traversal));
});

document.getElementById("refreshTreeBtn").addEventListener("click", async () => {
  highlightedPath = null;
  await loadTree();
  statusMessage.textContent = "Tree refreshed.";
  searchResult.textContent = "No search performed yet.";
});

loadTree().catch((error) => {
  statusMessage.textContent = error.message;
});
