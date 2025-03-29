# cart/tests/test_cart.py

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from cart.models import CartItem
from store.models import Product, Category, Subcategory

class CartAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name="Овощи", slug="ovoshi", image="cat.jpg")
        self.subcategory = Subcategory.objects.create(
            category=self.category, name="Корнеплоды", slug="korn", image="sub.jpg"
        )
        self.product = Product.objects.create(
            subcategory=self.subcategory,
            name="Морковь",
            slug="morkov",
            image_small="s.jpg",
            image_medium="m.jpg",
            image_large="l.jpg",
            price=30
        )

    def test_get_empty_cart(self):
        response = self.client.get("/api/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_items"], 0)
        self.assertEqual(response.data["total_price"], 0)



    def test_post_add_same_item_twice(self):
        self.client.post('/api/cart/', {'product_id': self.product.id, 'quantity': 2}, format='json')
        response = self.client.post('/api/cart/', {'product_id': self.product.id, 'quantity': 3}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['quantity'], 5)

    def test_add_to_cart(self):
        response = self.client.post("/api/cart/", {
            "product_id": self.product.id,
            "quantity": 3
        }, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["quantity"], 3)

    def test_update_nonexistent_cart_item(self):

        fake_id = 999  # Предполагаем, что такого ID нет
        response = self.client.put(f"/api/cart/{fake_id}/", {
            "quantity": 2
        }, format="json")

        self.assertEqual(response.status_code, 404)

    def test_post_add_to_cart_success(self):

        response = self.client.post("/api/cart/", {
            "product_id": self.product.id,
            "quantity": 2
        }, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["quantity"], 2)

    def test_post_add_to_cart_invalid_product(self):

        response = self.client.post("/api/cart/", {
            "product_id": 999,  # такого продукта нет
            "quantity": 1
        }, format="json")

        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.data)