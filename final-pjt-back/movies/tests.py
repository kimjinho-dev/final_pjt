from django.test import TestCase
from .models import Movie, Genre
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from .serializers import (
    MovieSerializer,
    MovieListSerializer,
    GenreSerializer,
    MovieMatchingGenreSerializer,
)
from rest_framework.decorators import api_view


@api_view()
def datatest(request):
    # moviegenres = get_object_or_404(Movie, pk=671)
    # serializer = MovieSerializer(moviegenres)
    genres = get_object_or_404(Genre, pk=28)

    # print(genres.name)
    # print(genres.genres)
    # print(genres.genres.all())
    # for g in genres.genres.all():
    #     print(g.title)

    # genrematching_data = []
    # print(genres.movies.all())
    # temp = list(genres.movies.all().values())
    # for g in temp:
    #     id_num = int(g['id'])
    #     movie = Movie.objects.get(pk=id_num)
    #     tmp = {
    #         'model': 'movies.movies',
    #         'pk': movie.id,
    #         'fields': {'title': movie.title},
    #     }
    #     genrematching_data.append(tmp)
    # print(genrematching_data)
    # genrematching_data.append(Movie.objects.get(pk=int(g['id'])))
    # serializer = GenreSerializer(genres.movies.all(), many=True)  # 해당 장르에 맞는 영화 ID 출력
    serializer = MovieSerializer(genres.movies.all(), many=True)  # 해당 장르에 맞는 영화 타이틀 출력
    return Response(serializer.data)
