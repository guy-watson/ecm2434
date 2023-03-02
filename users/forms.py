from django import forms
from django.contrib.auth.models import User
from .models import FriendRequest
from django import forms


class FriendRequestForm(forms.ModelForm):
    recipient = forms.CharField()

    class Meta:
        model = FriendRequest
        fields = []

    def clean_recipient(self):
        recipient_username = self.cleaned_data['recipient']
        try:
            recipient = User.objects.get(username=recipient_username)
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid username')
        return recipient

    def save(self, sender):
        recipient = self.cleaned_data['recipient']
        friend_request = FriendRequest(sender=sender, recipient=recipient)
        friend_request.save()
