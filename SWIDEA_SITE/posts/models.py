from django.db import models

class Post(models.Model):
    TOOL_CHOICE = (
        ('default', '----------'),
        ("DJANGO", "django"),
        ("REACT", "react"),
        ("SPRING", "Spring"),
        ("NODEJS","Node.js"),
        ("JAVA","Java"),
        ("CPP", "C++")
    )
    title = models.CharField(max_length= 100, verbose_name="제목")
    photo = models.ImageField(
        blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
    content = models.TextField(verbose_name="내용")
    interest = models.IntegerField(default=0,verbose_name="가격")
    devTools = models.CharField(max_length=20, choices=TOOL_CHOICE, default=TOOL_CHOICE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
