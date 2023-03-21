from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    id = models.AutoField(primary_key=True)

    
    def __str__(self):
        return self.username
    