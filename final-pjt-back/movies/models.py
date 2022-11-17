from django.db import models


class Movie(models.Model):
    # movieId = models.IntegerField()           # pk값으로 대체
    title = models.CharField(max_length=100)  # 영화제목
    overview = models.TextField()  # 줄거리
    # genre = models.TextField()                 # 장르(1-n 혹은 join으로 묶기)
    genre_ids = models.ManyToManyField('Genre', related_name='movies')
    poster_path = models.TextField()  # 포스터 url
    vote_average = models.FloatField()  # 평점
    release_date = models.TextField()  # 개봉일자
    # like_users = models.
    # runtime = models.IntegerField()           # 상영시간(detail 추출필요)


class Genre(models.Model):
    name = models.CharField(max_length=20)
