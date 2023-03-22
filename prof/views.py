# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.shortcuts import render
from leaderboard.models import Score
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from friendship.models import Friend, Follow, Block , FriendshipRequest



# Profile view
def profile(request):
    user = request.user
    # Get the score of the current user
    score = Score.objects.filter(player_name=user).values_list('score', flat=True).first()
    context = {'user': user, 'score': score}
    # Render the template with the user and the score and return it as a HttpResponse
    return render(request, 'profile/index.html', context)

# Toggle privacy view
def toggle_privacy(request):
    # Retrieve the current user's Score instance
    score = Score.objects.get(player_name=request.user)
    
    # Toggle the privacy option
    score.privacy = not score.privacy
    
    # Save the updated Score instance to the database
    score.save()

    return redirect('/leaderboard/')

# Add friend view
def add_friend(request):
    other_user = User.objects.get(pk=1)
    Friend.objects.add_friend(
        request.user,                              
        other_user,
    )
    return redirect('/leaderboard/')

# Friend requests view
def friend_requests(user):
    return {'friend_requests': Friend.objects.requests(user)}



    



