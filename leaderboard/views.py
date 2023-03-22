# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.shortcuts import render
from django.http import HttpResponse
from .models import Score
from django.template import loader
from django.shortcuts import redirect
from friendship.models import Friend, Follow, Block

# Leaderboard view
def leaderboard(request):
    # Get the top 10 scores and order them
    scores = Score.objects.order_by('-score')[:10]
    # Assign the template 
    template = loader.get_template('leaderboard/index.html')
    # Check if for each score the privacy is set to true
    for score in scores:
        if score.privacy == True:
            # If the privacy is true, set the player name to Anonymous
            score.player_name = 'Anonymous'
    # Assign the template and the context
    context = {
        'scores': scores
    }        
    # Render the template with the scores and return it as a HttpResponse
    return HttpResponse(template.render(context, request))



# Friend leaderboard view
def friendLeaderboard(request):
    friends = Friend.objects.friends(request.user)
    friend_scores = []

    friend_scores = Score.objects.filter(player_name__in=friends).order_by('-score')[:10]

    # Assign the template and the context
    template = loader.get_template('leaderboard/friends.html')
    context = {
        'friend_scores': friend_scores
    }
    # Render the template with the friend scores and return it as a HttpResponse
    return HttpResponse(template.render(context, request))