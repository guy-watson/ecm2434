# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.urls import path
from .views import leaderboard, friendLeaderboard

# Create the url for the leaderboard app
urlpatterns = [
    path('', leaderboard, name='index'),
    path('friends', friendLeaderboard, name='friend')
]
