from django.db import models
from django.contrib.auth.models import AbstractUser
from .read_time import calculate_reading_time


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
    estimated_read_time = models.IntegerField()

    def save(self, *args, **kwargs):
        self.estimated_read_time = calculate_reading_time(self.body)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_commented']  # Orders by the date commented in descending order (latest first)