from rest_framework import serializers
from shopping.models import *


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('user', 'id', 'name', 'create_date')
        read_only_fields = ('id',)


class ShoppingItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItems
        fields = ('id_shopping_list', 'id', 'name', 'quantity', 'image', 'descriptions', 'complete', 'created_at')
        read_only_fields = ('id', )