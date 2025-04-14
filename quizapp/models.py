from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()  # 1-4

    def __str__(self):
        return self.text

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    percentage = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
