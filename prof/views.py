# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
from leaderboard.models import Score
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import FriendRequest, UserProfile

def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile/index.html', context)


@method_decorator(login_required, name='dispatch')
class AcceptFriend(View):
    def post(self, request):
        from_user_id = request.POST.get('from_user_id')
        from_user = get_object_or_404(User, id=from_user_id)
        user_profile = UserProfile.objects.get(user=request.user)
        friend_request = FriendRequest.objects.get(from_user=from_user, to_user=user_profile.user)
        friend_request.is_accepted = True
        friend_request.save()
        user_profile.friends.add(from_user)
        return redirect('profile', username=request.user.username)
    
@method_decorator(login_required, name='dispatch')
class AddFriend(View):
    def post(self, request):
        to_user_id = request.POST.get('to_user_id')
        to_user = get_object_or_404(User, id=to_user_id)
        from_user = request.user
        friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        return redirect('profile', username=request.user.username)


