
from rest_framework.response import Response
# from rest_framework.decorators import api_view

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

# from rest_framework import status
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie


from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
import requests
import os
import json
from django.http import HttpResponseForbidden 
# from .models import Article
# from .models import Comment

class URLMaker:
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()

        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None

    def get_movie_url(self, category='movie', feature='popular', page='1'):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}&language=ko-KR&page={str(page)}'
        return url    

    def get_genre_url(self):
        url = f'{self.url}/genre/movie/list?api_key={self.key}'
        return url

    # def get_popular_url(self):    ## 이미 영화 데이터 가져온게 popular
    #     url = f'{self.url}/movie/popular?api_key={self.key}&language=ko-KR&page=1'
    #     return url

    def get_smilarMovie_url(self,movieId):
        url = f'{self.url}/movie/{movieId}/similar?api_key={self.key}&language=ko-KR&page=1'
        return url

TMDB_KEY = '0bdf8c1af69dea38be1f8564ad3e8265'
url = URLMaker(TMDB_KEY)

def movies(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         # serializer.save()
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

def dumpMovieDataGet(request):
#     TMD_KEY = '0bdf8c1af69dea38be1f8564ad3e8265'
#     LIST_URL = f"https://api.themoviedb.org/3/movie/popular?api_key={TMD_KEY}&language=ko-KR"
#     listData = requests.get(LIST_URL)
#     resDatas = listData.json().get('results')
#     # serializer = MovieSerializer(resDatas, many=True)
#     with open('./movies/fixtures/movies_data.json', 'w', encoding='utf-8') as file:
#         json.dump(resDatas, file, indent="\t", ensure_ascii=False)                      # 인기영화 100개 fixtures
#     # serializer = MovieListSerializer(movies, many=True)
#     # print(resDatas)
#     # print(serializer)
#     # return Response(serializer)
#     # print(resDatas)
#     # print('뭐야')
#     # while(resDatas):
#     #     movie = Movie()
#     #     resData = resDatas.pop()
#     #     # movie = MovieSerializer(resData)
#     #     # print(",".join(map(str, resData['genre_ids']))
#     #     movie.title = resData['title']
#     #     movie.overview = resData['overview']        
#     #     movie.genres = ",".join(map(str, resData['genre_ids']))
#     #     movie.movieId = resData['id']
#     #     movie.poster_url = resData['poster_path']
#     #     movie.vote_average = resData['vote_average']
#     #     movie.release_date = resData['release_date']
#     #     with open('./movies/fixtures/movies_data.json', 'w', encoding='utf-8') as file:
#     #         json.dump(movie, file, indent="\t", ensure_ascii=False)
#     #     # movie.runtime = resData.id
#     #     # print(movie)
#     #     # movie.save()

    create_genre_data()
    create_movie_data()
    return redirect('..')

def create_genre_data():
    genre_url = url.get_genre_url()
    raw_data = requests.get(genre_url)
    json_data = raw_data.json()
    genres = json_data.get('genres')

    genre_data = []

    for genre in genres:
        tmp = {
            'model': 'movies.genre',
            'pk': genre['id'],
            'fields': {
                'name': genre['name']
            }
        }
        genre_data.append(tmp)

    with open('./movies/fixtures/genres.json', 'w') as f:
        json.dump(genre_data, f, indent=4, ensure_ascii=False)

def create_movie_data():
    # with open('./movies/fixtures/genres.json', 'r+') as f:
    #     movie_data = json.load(f)

    movie_data = []
    # for page in range(1, 501):
    for page in range(1, 10):
        raw_data = requests.get(url.get_movie_url(page=page))
        json_data = raw_data.json()
        movies = json_data.get('results')

        for movie in movies:
            if movie.get('release_date') == "" or movie.get('poster_path') == "":
                continue

            movie.pop('adult')
            movie.pop('original_language')
            movie.pop('original_title')
            movie.pop('popularity')
            movie.pop('backdrop_path')
            movie.pop('video')
            movie.pop('vote_count')
            # movie['like_users'] = []
            tmp = {
                'model': 'movies.movie',
                'pk': movie.pop('id'),
                'fields': movie,
            }
            movie_data.append(tmp)

    with open('./movies/fixtures/movies.json', 'w', encoding='utf-8') as f:
        json.dump(movie_data, f, indent=4, ensure_ascii=False)


