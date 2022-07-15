from django.db import models

class Post(models.Model):
    GENRE_CHOICES = { ('romance','로맨스'), ('crime','범죄'), ('comedy','코미디'),('action','액션'),('thriller','스릴러'),('SF','SF'),('horror','공포')}
    
    title = models.CharField(max_length= 100, verbose_name="제목")
    release_year = models.IntegerField(verbose_name="개봉 년도")
    genre = models.CharField(max_length= 100, verbose_name="장르", choices=GENRE_CHOICES)
    rate = models.FloatField(verbose_name="별점")
    director = models.CharField(max_length= 100, verbose_name="감독")
    main = models.CharField(max_length= 100, verbose_name="주연")
    running_time = models.IntegerField(verbose_name="러닝타임")
    review = models.TextField(verbose_name="리뷰")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)