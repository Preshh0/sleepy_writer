from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post = models.TextField()
    author = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self): #adding str() method to models is best practice and also makes your code more readable.
        return self.post_title