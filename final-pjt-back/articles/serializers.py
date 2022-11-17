from rest_framework import serializers
from .models import Community, CommunityTag, Foods
# from .models import Comment


class CommunityListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Community
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'user', 'username', 'tags')
        read_only_fields = ('user', )

class CommunityTagSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CommunityTag
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class CommunitySerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    tags = CommunityTagSerializer(many=True)

    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ('user', )




class FoodsListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Foods
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'user', 'username', 'tags')
        read_only_fields = ('user', )

class FoodsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CommunityTag
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class FoodsSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    tags = FoodsTagSerializer(many=True)

    class Meta:
        model = Foods
        fields = '__all__'
        read_only_fields = ('user', )


# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('article',)






