from django.db import models

class DevTool(models.Model):
    name = models.CharField(max_length=50, verbose_name="이름")
    kind = models.CharField(max_length=50, verbose_name="종류")
    content = models.TextField(verbose_name="설명")

class Post(models.Model):
    title = models.CharField(max_length= 100, verbose_name="제목")
    photo = models.ImageField(
        blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
    content = models.TextField(verbose_name="내용")
    interest = models.IntegerField(default=0,verbose_name="관심도")
    test = models.ForeignKey(DevTool,
                             on_delete=models.CASCADE,
                             related_name="post_tool")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


