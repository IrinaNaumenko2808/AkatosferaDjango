document.addEventListener("DOMContentLoaded", () => {
  loadCategories();
  loadProducts();

  document.getElementById("categorySelect").addEventListener("change", () => {
    const categoryId = document.getElementById("categorySelect").value;
    loadProducts(categoryId);
  });
});

function loadCategories() {
  fetch("http://127.0.0.1:8000/api/categories/")
    .then(response => response.json())
    .then(data => {
      const select = document.getElementById("categorySelect");
      data.results.forEach(cat => {
        const option = document.createElement("option");
        option.value = cat.id;
        option.textContent = cat.name;
        select.appendChild(option);
      });
    });
}

function loadProducts(categoryId = "") {
  let url = "http://127.0.0.1:8000/api/products/";
  if (categoryId) {
    url += `?category=${categoryId}`;
  }

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById("products-list");
      list.innerHTML = "";
      data.results.forEach(product => {
        const card = document.createElement("div");
        card.className = "col-md-4 mb-4";
        card.innerHTML = `
          <div class="card h-100">
            <img src="${product.images[0]}" class="card-img-top" alt="${product.name}">
            <div class="card-body">
              <h5 class="card-title">${product.name}</h5>
              <p class="card-text">${product.price} ₽</p>
              <button class="btn btn-success" onclick="addToCart(${product.id})">Добавить в корзину</button>
            </div>
          </div>
        `;
        list.appendChild(card);
      });
    });
}
