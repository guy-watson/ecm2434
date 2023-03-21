# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.urls import path
from .views import leaderboard

urlpatterns = [
    path('', leaderboard, name='index'),

]
