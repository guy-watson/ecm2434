# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.urls import path
from .views import team_list

urlpatterns = [
    path('', team_list, name='index'),
    
]
