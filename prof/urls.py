# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.urls import path, re_path
from .views import profile 
from . import views
from django.urls import include 

# Create the urls for the profile app
urlpatterns = [
    path('', profile, name='index'),
    path('toggle_privacy', views.toggle_privacy, name='toggle_privacy'),
    path('friendship/', include('friendship.urls')),
    path('add_friend', views.add_friend, name='add_friend'),
]
