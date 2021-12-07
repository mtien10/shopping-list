from django.urls import path
from app.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('hi', hello),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
]
