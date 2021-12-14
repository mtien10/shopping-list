from rest_framework import serializers
from shopping.models import *
from app.serializers import *


class ShoppingListSerializer(serializers.ModelSerializer):
    share_users = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = ShoppingList
        fields = ('user', 'id', 'name', 'create_date', 'share_users')
        read_only_fields = ('id',)


class ListDetailSerializer(ShoppingListSerializer):
    share_users = UserSerializer(many=True, read_only=True)


class ShoppingItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItems
        fields = ('id_shopping_list', 'id', 'name', 'quantity', 'image', 'descriptions', 'complete', 'created_at')
        read_only_fields = ('id',)
