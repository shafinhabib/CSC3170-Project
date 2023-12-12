from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', blank=True, null=True, default='blank-profile-picture.png')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    

class Message(models.Model):
    """Message"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='用户')
    message = models.TextField(verbose_name='Message')
    add_time = models.DateTimeField(verbose_name='time',default=datetime.now)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message

class Category(models.Model):
    name = models.CharField(verbose_name='doc classification',max_length=20)
    add_time = models.DateTimeField(verbose_name='Createtime',default=datetime.now)
    edit_time = models.DateTimeField(verbose_name='Modifytime',default=datetime.now)

    class Meta:
        verbose_name = 'doc classification'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

