# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.urls import path
from .views import leaderboard, friendLeaderboard
from . import views

# Create the url for the leaderboard app 
urlpatterns = [
    path('', leaderboard, name='index'),
    path('leaderboard/friends', views.friendLeaderboard, name='friend')
]
