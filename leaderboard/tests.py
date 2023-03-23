# Aurthor: Kaloyan Gaydarov and Taariq Fadhill 
from django.test import TestCase , Client
from .models import Score

# Test class for the leaderboard app
class LeaderboardTests(TestCase):
    # Set up the client and a score
    def setUp(self):
        self.client = Client()
        self.score = Score.objects.create(player_name='test', score=100)
        
    # Test the leaderboard view
    def test_leaderboard(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard/index.html')

    # Test the leaderboard view with a score
    def test_leaderboard_with_score(self):
        response = self.client.get('/leaderboard/')
        self.assertContains(response, 'test')
        self.assertContains(response, '100')

    # Test the leaderboard view with a user
    def test_leaderboard_with_user(self):
        self.client.login(username='test', password='test')
        response = self.client.get('/leaderboard/')
        self.assertContains(response, 'test')
        self.assertContains(response, '100')

    # Test the leaderboard view with a user and score
    def test_leaderboard_with_user_and_score(self):
        self.client.login(username='test', password='test')
        response = self.client.get('/leaderboard/')
        self.assertContains(response, 'test')
        self.assertContains(response, '100')

        

    




