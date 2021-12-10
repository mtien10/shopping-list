from rest_framework import viewsets, permissions, mixins
from shopping.serializers import ShoppingListSerializer
from shopping import serializers
from shopping.models import ShoppingList


class ShoppingListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShoppingListSerializer
    queryset = ShoppingList.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=1)

    # def perform_create(self, serializer):
    #     serializer.save(id=self.request.user.id)

    # def perform_destroy(self, instance):
    #     instance.delete()



