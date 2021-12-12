from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response

from shopping.serializers import ShoppingListSerializer
from shopping import serializers
from shopping.models import ShoppingList


class ShoppingListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShoppingListSerializer
    queryset = ShoppingList.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request['user_id']
        return self.queryset.filter(user=user_id)



        # print(self.request.user)
        # try:
        #     isAuthenticated = self.request.session['is-authenticated']
        #     if (isAuthenticated):
        #         userId = self.request.session['user_id']
        #         return self.queryset.filter(user=userId)
        #     else:
        #         pass
        # except Exception as e:
        #     pass

    

    # def perform_create(self, serializer):
    #     serializer.save(id=self.request.user.id)


