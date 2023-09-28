import random
from django.shortcuts import render
from django.views.generic import ListView, DetailView # 여러 포스트를 나열할 때.
from .models import Post

# class PostList(ListView):
#     """
#     ListView를 사용할 것이고 model은 Post다. 선언
#     """
#     model = Post
#     ordering = '-pk' # pk값이 작은 순서대로(최신글) 보여줘라
    

# class PostDetail(DetailView):
#     model = Post
 


def news_list(request):
    selected_questions = request.session.get('quest3')
    
    return render(request, 'news/post_list.html', {'selected_questions': selected_questions})

