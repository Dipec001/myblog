from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_commented']  # Orders by the date commented in descending order (latest first)