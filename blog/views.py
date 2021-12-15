from typing import List
from django.views.generic import ListView
from .models import Post

# Create your views here.

class Blog(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'all_posts_list'