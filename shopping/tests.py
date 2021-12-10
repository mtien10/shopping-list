from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import test, status
from rest_framework.test import APIClient

from shopping.models import ShoppingList

from shopping.serializers import ShoppingListSerializer

SHOPPINGLIST_URL = reverse('shopping:shopping-list')


def sample_shopping(user, **params):
    defaults = {
        'user': 1,
        'name': 'tien',
        'create_date': '1753-01-01 9:12:31'
    }
    defaults.update(params)
    return ShoppingList.objects.create(user=user, **defaults)


class PublicShoppingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(SHOPPINGLIST_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateShoppingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'tien@gmail.com'
            'test'
        )
        self.client.force_authenticate(self.user)

    def test_retrive_shopping(self):
        sample_shopping(user=self.user)
        sample_shopping(user=self.user)

        res = self.client.get(SHOPPINGLIST_URL)

        shoppings = ShoppingList.objects.all().order_by('-id')
        serializer = ShoppingListSerializer(shoppings, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_shoppings_limited_to_user(self):
        user2 = get_user_model().objects.create_user(
            'tien1@gmail.com'
            'tien'
        )
        sample_shopping(user=user2)
        sample_shopping(user=self.user)

        res = self.client.get(SHOPPINGLIST_URL)

        shoppings = ShoppingList.objects.filter(user=self.user)
        serializer = ShoppingListSerializer(shoppings, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)



