from django.db import models

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    headline = models.CharField(max_length=100)
    lead = models.TextField()
    invest = models.CharField(max_length=30)
    answer = models.BooleanField()


class Rank(models.Model):
    nickname = models.CharField(max_length=255)
    score = models.IntegerField()
    rank = models.IntegerField(default=0)  # 기본값을 0으로 설정

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['-score', '-id']  # 점수를 기준으로 내림차순으로 정렬하고, id를 기준으로 내림차순으로 정렬
