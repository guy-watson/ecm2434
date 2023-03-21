# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class User(AbstractUser):
    # custom fields and methods here

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='prof_users' # add a related_name here
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='prof_users' # add a related_name here
    )


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.from_user.username
    
    class Meta:
        unique_together = ('from_user', 'to_user')

        
    

        