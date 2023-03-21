# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.db import models

# Define the score model class
class Score(models.Model):
    # Fields of player name and score
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()

# from leaderboard.models import Score
# new_score = Score(player_name='Player 1', score=100)
# new_score.save()

#score = Score.objects.get(player_name='Player 1')
#score.score += 50
#score.save()
#Score.objects.filter(player_name='Player 1').update(score=models.F('score') + 50)
