from django.test import TestCase, Client
from leaderboard.models import Score
from django.contrib.auth.models import User
from views import toggle_privacy

class Test(TestCase):
    # Set up the client and a score
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')
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

    # Test the leaderboard view with a user and score and post
    def test_leaderboard_with_user_and_score_and_post(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/leaderboard/', {'player_name': 'test', 'score': 100})
        self.assertContains(response, 'test')
        self.assertContains(response, '100')

    # toggle_privacy
    def test_leaderboard_privacy(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/leaderboard/', {'player_name': 'test', 'score': 100})
        toggle_privacy(self)
        response = self.client.get('/leaderboard/')
        self.assertContains(response, 'Annoymous')
        self.assertContains(response, '100')
        


    

    