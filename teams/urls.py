# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.urls import path
from .views import add_member, team_detail

app_name = 'teams'
urlpatterns = [
    path('add_member/', add_member, name='add_member'),
]