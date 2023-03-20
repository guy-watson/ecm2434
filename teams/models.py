# Aurthor: Kaloyan Gaydarov and Taariq Fadhill
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_teams',default=1)

    def __str__(self):
        return self.name

