from django.urls import path
from . import views

"""
끝이 /news/ 로 끝날 때는 PostList가 처리
"""

urlpatterns = [
    # path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.news_list, name='news_feed'),
]



