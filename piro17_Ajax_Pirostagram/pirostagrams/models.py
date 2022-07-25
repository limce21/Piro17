from django.db import models
from django.db import models
   
class Post(models.Model):
   content = models.TextField(blank=True, verbose_name="글", default="")
   location = models.CharField(max_length=50, verbose_name="지역")
   like = models.BooleanField(default=False, verbose_name="좋아요")

   
class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_user")
   comment = models.CharField(max_length=255, verbose_name="댓글")