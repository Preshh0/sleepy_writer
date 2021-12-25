from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import CustomUser

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post = models.TextField()
    author = models.ForeignKey( #foreignkey allows for many-to-one relationships for the author. i.e one author can have many posts. but one post can't have many authors.
        'accounts.CustomUser', #this worked cos i did 'theappname.themodelclassname'
        on_delete=models.Case #important for many-to-one relationships
    )
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self): #adding str() method to models is best practice and also makes your code more readable.
        return self.post_title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])