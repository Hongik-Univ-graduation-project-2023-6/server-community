from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # post_user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='user_posts'
    # )
    username = models.CharField(default='anonymous', max_length=50, blank=False)
    title = models.TextField(max_length=1000, blank=False)
    content = models.TextField(max_length=2000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_images'
    )
    image_file = models.ImageField(upload_to='images')

class Comment(models.Model):
    # comment_user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='user_comments'
    # )
    username = models.CharField(default='anonymous', max_length=50, blank=False)
    comment_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comments'
    )
    content = models.TextField(max_length=2000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
