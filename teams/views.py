from django.shortcuts import render, redirect
from .models import Team

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/add_member.html', {'teams': teams})


