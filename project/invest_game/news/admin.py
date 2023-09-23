from django.contrib import admin
from .models import Post

# 관리자 페이지에 Post 모델 등록하기
admin.site.register(Post)