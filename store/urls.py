from django.urls import path
from .views import CategoryListView, ProductListView
from .views import register_user

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('register/', register_user),
]