from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def blogPost(request):
    context = {
        'blog_title': "This is a title!",
        'blog_post': "This is a post!"
    }
    return render(request, 'blog/index.html', request)

# def trial(request, post_id):
#     return HttpResponse('This is post' %post_id)