from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('quiz.urls')), 
    path('news/', include('news.urls')),
    path('quiz/', include('quiz.urls')),
]
