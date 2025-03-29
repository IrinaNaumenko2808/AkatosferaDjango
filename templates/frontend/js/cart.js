document.addEventListener('DOMContentLoaded', loadCart);

function loadCart() {
  fetch('http://127.0.0.1:8000/api/cart/summary/', {
    headers: {
      'Authorization': `Token ${token}`
    }
  })
    .then(response => response.json())
    .then(data => {
      const cartItemsContainer = document.getElementById('cart-items');
      const cartSummary = document.getElementById('cart-summary');
      cartItemsContainer.innerHTML = '';

      if (data.items.length === 0) {
        cartItemsContainer.innerHTML = '<p>Корзина пуста.</p>';
        cartSummary.textContent = '';
        return;
      }

      data.items.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('border', 'p-3', 'mb-2');
        itemElement.innerHTML = `
          <h5>${item.product.name}</h5>
          <p>Цена: ${item.product.price}₽</p>
          <p>Количество: ${item.quantity}</p>
        `;
        cartItemsContainer.appendChild(itemElement);
      });

      cartSummary.textContent = `Всего товаров: ${data.total_items}, Общая сумма: ${data.total_price}₽`;
    })
    .catch(error => {
      console.error('Ошибка при загрузке корзины:', error);
    });
}

function clearCart() {
  fetch('http://127.0.0.1:8000/api/cart/clear/', {
    method: 'DELETE',
    headers: {
      'Authorization': `Token ${token}`
    }
  })
    .then(response => {
      if (response.ok) {
        alert('Корзина очищена!');
        loadCart();
      } else {
        alert('Не удалось очистить корзину');
      }
    })
    .catch(error => {
      console.error('Ошибка при очистке корзины:', error);
    });
}

