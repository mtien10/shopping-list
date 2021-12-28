from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response
from shopping.serializers import ShoppingListSerializer
from shopping import serializers
from shopping.models import ShoppingList, ShoppingItems
from rest_framework.decorators import api_view
from app.models import *


class ShoppingListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShoppingListSerializer
    queryset = ShoppingList.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ListDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
def share_shopping_list(request, pk):
    user_ids = request.data.get('user_ids', [])
    shopping_list = ShoppingList.objects.get(pk=pk)
    for user_id in user_ids:
        shopping_list.share_users.add(User.objects.get(pk=user_id))


class ShoppingItemsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShoppingItemsSerializer
    queryset = ShoppingItems.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id_shopping_list__user=self.request.user)
