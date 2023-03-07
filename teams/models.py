# Aurthor: Kaloyan Gaydarov and Taariq Fadhill
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, through='Membership')
    
    def __str__(self):
        return self.name

class Membership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} is a member of {self.team.name}"