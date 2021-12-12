from django.contrib import admin
from shopping.models import *
from shopping import models

admin.site.register(models.ShoppingList)


@admin.register(ShoppingItems)
class ShoppingItemsAdmin(admin.ModelAdmin):
    list_display = ("name", "complete", "created_at", "id_shopping_list")
