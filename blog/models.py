from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class BlogPost(models.Model):
    post_title = models.CharField(max_length=20)
    post = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=40)

    def __str__(self): #the str function helps output readable text to the computer screen
        return self.post 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comments(models.Model):
    comment = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text=models.CharField(max_length=30)
    author=models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post