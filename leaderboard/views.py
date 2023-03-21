# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.shortcuts import render
from django.http import HttpResponse
from .models import Score
from django.template import loader

# Leaderboard view
def leaderboard(request):
    # Get the top 10 scores and order them
    scores = Score.objects.order_by('-score')[:10]
    # Assign the template and the context
    template = loader.get_template('leaderboard/index.html')
    context = {
        'scores': scores
    }
    # Render the template with the scores and return it as a HttpResponse
    return HttpResponse(template.render(context, request))

# Friend leaderboard view
def friendLeaderboard(request):
    # Get the top 10 scores and order them
    scores = Score.objects.order_by('-score')[:10]
    # Assign the template and the context
    template = loader.get_template('leaderboard/friends.html')
    context = {
        'scores': scores
    }
    # Render the template with the scores and return it as a HttpResponse
    return HttpResponse(template.render(context, request))

    # if request.user.is_authenticated:
    #     # Get the user's friends
    #     friends = Friend.objects.filter(user=request.user)
    #     friend_scores = []
    #     for friend in friends:
    #     # For each friend, get their top score and add it to the list
    #     friend_score = Score.objects.filter(player_name=friend.friend_name).order_by('-score').first()
    #     if friend_score:
    #     friend_scores.append(friend_score)
    #     # Sort the list of friend scores
    #     friend_scores = sorted(friend_scores, key=lambda x: x.score, reverse=True)
    #     # Assign the template and the context
    #     template = loader.get_template('leaderboard/friends.html')
    #     context = {
    #     'friend_scores': friend_scores
    #     }
    #     # Render the template with the friend scores and return it as a HttpResponse
    #     return HttpResponse(template.render(context, request))
    # else:
    #     # If the user is not logged in, redirects to login page.
    #     return HttpResponse(template.render(request, 'login.html'))
