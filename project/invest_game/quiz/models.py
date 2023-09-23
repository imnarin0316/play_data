from django.db import models

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    headline = models.CharField(max_length=100)
    lead = models.TextField()
    invest = models.CharField(max_length=30)
    answer = models.BooleanField()
