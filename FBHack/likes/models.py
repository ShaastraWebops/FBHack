from django.db import models
from users.models import FBUserProfile
from FBHack.models import FBPosts
# Create your models here.

class FBPosts(models.Model):
  desc = models.CharField(max_length = 500)
  post_id = models.CharField(max_length = 50)
  link = models.CharField(max_length = 500)
  likes = models.IntegerField(default=0)
  shares = models.IntegerField(default=0)
  likes_given = models.IntegerField(default=0)
  shares_given = models.IntegerField(default=0) 

class likes(models.Model):
  like_id = models.CharField(max_length = 50)
  postId = models.ForeignKey(FBPosts, related_name="post")
  user_id = models.ForeignKey(FBUserProfile)