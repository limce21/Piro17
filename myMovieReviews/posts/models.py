from django.db import models

class Post(models.Model):
    title = models.CharField(max_length= 100, verbose_name="제목")
    release_year = models.IntegerField(verbose_name="개봉 년도")
    genre = models.CharField(max_length= 100, verbose_name="장르")
    rate = models.FloatField(verbose_name="별점")
    director = models.CharField(max_length= 100, verbose_name="감독")
    main = models.CharField(max_length= 100, verbose_name="주연")
    running_time = models.IntegerField(verbose_name="러닝타임")
    review = models.TextField(verbose_name="리뷰")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)