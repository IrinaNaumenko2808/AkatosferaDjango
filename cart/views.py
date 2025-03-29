
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from .models import CartItem
from .serializers import CartItemSerializer
from store.models import Product
from rest_framework.decorators import action



class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]



    def list(self, request):
        items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(items, many=True)
        total_items = sum(item.quantity for item in items)
        total_price = sum(item.product.price * item.quantity for item in items)
        return Response({
            'items': serializer.data,
            'total_items': total_items,
            'total_price': total_price
        })

    def create(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response({"error": "product_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            cart_item = CartItem.objects.get(pk=pk, user=request.user)
        except CartItem.DoesNotExist:
            return Response(status=404)

        quantity = int(request.data.get('quantity', 1))
        cart_item.quantity = quantity
        cart_item.save()
        return Response(CartItemSerializer(cart_item).data)

    def destroy(self, request, pk=None):
        try:
            cart_item = CartItem.objects.get(pk=pk, user=request.user)
        except CartItem.DoesNotExist:
            return Response(status=404)
        cart_item.delete()
        return Response(status=204)

    @action(detail=False, methods=['delete'])
    def clear(self, request):
        CartItem.objects.filter(user=request.user).delete()
        return Response({'message': 'Корзина очищена'}, status=204)

