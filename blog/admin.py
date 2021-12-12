from django.contrib import admin

# Register your models here.

from .models import BlogPost

admin.site.register(BlogPost) #this tells django to register this model in the admin interface