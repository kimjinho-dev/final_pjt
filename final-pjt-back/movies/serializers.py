from rest_framework import serializers
from .models import Movie
# from .models import Comment


class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'genres', 'poster_url', 'vote_average', 'release_date', 'runtime')




class MovieSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'genres', 'poster_url', 'vote_average', 'release_date', 'runtime')
        # read_only_fields = ('user', )