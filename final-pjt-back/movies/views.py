
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# permission Decorators
from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie


from django.shortcuts import render,redirect, get_object_or_404
import requests
import os
from django.http import HttpResponseForbidden 
# from .models import Article
# from .models import Comment

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

def movieget(request):
    TMD_KEY = '0bdf8c1af69dea38be1f8564ad3e8265'
    LIST_URL = f"https://api.themoviedb.org/3/movie/popular?api_key={TMD_KEY}&language=ko-KR"
    listData = requests.get(LIST_URL)
    resDatas = listData.json().get('results')
    # serializer = MovieSerializer(resDatas, many=True)
    with open('./movies/fixtures/movies_data.json', 'w', encoding='utf-8') as file:
        json.dump(resDatas, file, indent="\t", ensure_ascii=False)                      # 인기영화 100개 fixtures
    # serializer = MovieListSerializer(movies, many=True)
    # print(resDatas)
    # print(serializer)
    # return Response(serializer)
    # print(resDatas)
    # print('뭐야')
    # while(resDatas):
    #     movie = Movie()
    #     resData = resDatas.pop()
    #     # movie = MovieSerializer(resData)
    #     # print(",".join(map(str, resData['genre_ids']))
    #     movie.title = resData['title']
    #     movie.overview = resData['overview']        
    #     movie.genres = ",".join(map(str, resData['genre_ids']))
    #     movie.movieId = resData['id']
    #     movie.poster_url = resData['poster_path']
    #     movie.vote_average = resData['vote_average']
    #     movie.release_date = resData['release_date']
    #     with open('./movies/fixtures/movies_data.json', 'w', encoding='utf-8') as file:
    #         json.dump(movie, file, indent="\t", ensure_ascii=False)
    #     # movie.runtime = resData.id
    #     # print(movie)
    #     # movie.save()
    return redirect('..')
