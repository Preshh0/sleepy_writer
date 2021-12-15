from django.urls import path
from .views import Blog, BlogDetailView

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', Blog.as_view(), name='blog')
]