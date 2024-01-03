from django.contrib import admin
from .models import CustomUser, BlogPost, Comment

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BlogPost)
admin.site.register(Comment)