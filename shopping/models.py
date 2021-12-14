from django.db import models
from app.models import User


class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    share_users = models.ManyToManyField(User, related_name='share_users')

    def __str__(self):
        return self.name


class ShoppingItems(models.Model):
    id_shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='static/images')
    descriptions = models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

