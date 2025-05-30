from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


app_name = 'users'

urlpatterns = [
    path('login/', TokenLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UsersRegistration.as_view(), name='register'),
]