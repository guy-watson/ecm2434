from django.urls import path
from .views import register

urlpatterns = [
    path('login/', register, name='register'),
]