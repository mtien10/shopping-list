from rest_framework import serializers
from shopping.models import *


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('user', 'id', 'name', 'create_date')
        read_only_fields = ('id',)

