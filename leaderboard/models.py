# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.db import models

# Define the score model class
class Score(models.Model):
    # Fields of player name and score
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()