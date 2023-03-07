# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.urls import path
from .views import profile

urlpatterns = [
    path('', profile, name='index'),
    
]
