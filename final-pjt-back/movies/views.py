from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie, Genre

from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
import requests
import json

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

    def get_movie_detail(self,movieId): # 영화 디테일
        url = f'{self.url}/movie/{movieId}/?api_key={self.key}&language=ko-KR'

    def get_genre_url(self):
        url = f'{self.url}/genre/movie/list?api_key={self.key}'
        return url

    # def get_popular_url(self):    ## 이미 영화 데이터 가져온게 popular
    #     url = f'{self.url}/movie/popular?api_key={self.key}&language=ko-KR&page=1'
    #     return url

    def get_smilarMovie_url(self,movieId):  # 유사영화(id필요)
        url = f'{self.url}/movie/{movieId}/similar?api_key={self.key}&language=ko-KR&page=1'
        return url

TMDB_KEY = '0bdf8c1af69dea38be1f8564ad3e8265'
url = URLMaker(TMDB_KEY)

@api_view(['GET'])
def movies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def genre(request,genre_id): # 해당 장르에 맞는 영화 출력
    genre = get_object_or_404(Genre, pk=genre_id)
    serializer = MovieSerializer(genre.movies.all(), many=True)  
    return Response(serializer.data)

# @api_view(['GET'])
# def smilar(request,movie_id): # 해당 영화와 비슷한 영화 출력(이건 뷰에서하는게 좋을거같은데?)
#     raw_data = requests.get(url.get_smilarMovie_url(movieId=movie_id))
#     json_data = raw_data.json()
#     serializer = MovieSerializer(json_data)
#     return Response(raw_data.data)

def dumpMovieDataGet(request):
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
