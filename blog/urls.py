from django.urls import path
from .views import Blog, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', Blog.as_view(), name='blog')
]