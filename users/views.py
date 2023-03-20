from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FriendRequestForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FriendRequest
from .forms import FriendRequestForm

@login_required
def send_friend_request(request):
    if request.method == 'POST':
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'Friend request sent')
            return redirect('profile', username=form.cleaned_data['recipient'].username)
    else:
        form = FriendRequestForm()

    return render(request, 'friends/send_friend_request.html', {'form': form})

@login_required
def add_friend(request):
    form = FriendRequestForm(request.POST or None)
    if form.is_valid():
        friend_username = form.cleaned_data.get('friend_username')
        friend = User.objects.get(username=friend_username)
        friend_request = FriendRequest(from_user=request.user, to_user=friend)
        friend_request.save()
        return redirect('friends')
    return render(request, 'users/add_users.html', {'form': form})
