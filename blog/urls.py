from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.blogPost, name="BlogPost"),
    # path('blog/<int:post_id>', views.trial, name="trial")
]


