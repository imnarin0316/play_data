from django.db import models


# models는 데이터를 저장하기 위한 하나의 단위

class Post(models.Model):
    """
    글쓰기 페이지에 넣을 데이터
    title : 뉴스피드 타이틀
    content : 뉴스피드 요약 내용
    created_at : 작성일
    author : 작성자 정보
    """

    # CharField : 최대 길이 정의 필요한 타입
    # TextField : 그 외
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # 년,월,일,시,초 기록 / auto_now_add=True 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True) #auto_now=True 다시 저장할 때마다 저장
    # author = 추후 작성 예정.

    # python manage.py makemigrations : 마이그레이션 등록


    def __str__(self):
        """
        self.pk : 해당 포스트의 pk 값. 자동생성되는 포스트의 id 값이라고 생각.
        self.title: 제목.
        """
        return f"[{self.pk}]{self.title}"
    
    def get_absolute_url(self):
        return f'/news/{self.pk}'
    
    