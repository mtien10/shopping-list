from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shopping import views

router = DefaultRouter()
router.register('shopping-list', views.ShoppingListViewSet)
router.register('items', views.ShoppingItemsViewSet)

app_name = 'shopping'

urlpatterns = [
    path('', include(router.urls))
]