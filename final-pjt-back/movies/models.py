from django.db import models

class Movie(models.Model):
    movieId = models.IntegerField() 
    title = models.CharField(max_length=100)    # 영화제목
    overview = models.TextField()               # 줄거리 
    genres = models.TextField()                 # 장르
    poster_url = models.URLField()              # 포스터 url
    vote_average = models.FloatField()          # 평점
    release_date = models.TextField()       # 개봉일자
    # runtime = models.IntegerField()             # 상영시간
    # tags = ArrayField(models.CharField(max_length=20), blank=True)
