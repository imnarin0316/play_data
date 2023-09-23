from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.answer_question, name='answer_question'),
    path('result/', views.view_quiz_result, name='quiz_result'),
    path('', views.start_game, name='start_game'),
]



