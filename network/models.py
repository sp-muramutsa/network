from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class User(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    portrait = models.URLField(null=True, blank=True)
    bio = models.TextField(max_length=600, null=True, blank=True)
    follows = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)

    def str(self):
        return f"{self.first_name} {self.last_name}"
    
    def following_count(self):
        return self.follows.count()
    
    def followers_count(self):
        return self.followers.count()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    content = models.TextField()
    likes =  models.ManyToManyField(User, related_name="liked_posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def like_count(self):
        return self.likes.count()
    
    def comment_count(self):
        return self.comments.count() 
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes =  models.ManyToManyField(User, related_name="liked_comments", blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    def like_count(self):
        return self.likes.count()
    
    def reply_count(self):
        return self.likes.count()