# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.test import TestCase , Client
from .models import Score

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.score = Score.objects.create(player_name='test', score=100)
        
    def test_leaderboard(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard.html')




