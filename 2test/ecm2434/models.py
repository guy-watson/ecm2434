from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_a = models.CharField(max_length=200)
    answer_b = models.CharField(max_length=200)
    answer_c = models.CharField(max_length=200)
    answer_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)
    
    def __str__(self):
        return self.question_text

    class Meta:
        app_label = 'ecm2434'
