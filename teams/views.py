from django.shortcuts import render, redirect
from .models import Team


def add_member(request):
    if request.method == 'POST':
        team_id = request.POST.get('team')
        team = Team.objects.get(pk=team_id)
        team.members.add(request.user)

        return redirect('teams:team_detail', team_id=team.id)
        
    else:
        teams = Team.objects.all()
        return render(request, 'teams/add_member.html', {'teams': teams})


def team_detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    members = team.members.all()
    return render(request, 'teams/team_detail.html', {'team': team, 'members': members})
