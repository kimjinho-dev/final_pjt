from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Genre
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

# class MovieGenerSerializer(serializers.ModelSerializer):
#     genre = serializers.CharField()
#     poster_path = serializers.CharField()


    # class Meta:
    #     model = Movie
    #     fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'

class MovieTopratedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['pk','title','poster_path',]

# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = '__all__'
#         read_only_fields = ('name',)
