from rest_framework import serializers
from .models import Movie, Genre

# from .models import Comment


class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('user', )


class GenreSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ('name',)


class MovieMatchingGenreSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = ('title',)
