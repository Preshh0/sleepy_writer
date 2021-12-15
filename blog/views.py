from typing import List
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class Blog(ListView):
    model = Post
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'