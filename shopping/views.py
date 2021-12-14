from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response
from shopping.serializers import ShoppingListSerializer
from shopping import serializers
from shopping.models import ShoppingList, ShoppingItems


class ShoppingListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShoppingListSerializer
    queryset = ShoppingList.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ShoppingItemsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShoppingItemsSerializer
    queryset = ShoppingItems.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id_shopping_list__user=self.request.user)





