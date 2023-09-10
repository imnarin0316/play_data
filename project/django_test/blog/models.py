from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True) #자동으로 시간 추가 auto_now_add
    udated_at = models.DateTimeField(auto_now=True) # 수정된 시간 자동으로 지금으로 변경
    #auther 추후 작성예정.

    def __str__(self):
        return f"[{self.pk}]{self.title}"
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    