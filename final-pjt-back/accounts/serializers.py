from rest_framework import serializers
from .models import User
# from .models import Comment

# class CommunityTagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = CommunityTag
#         fields = ['id', 'name']
#         extra_kwargs = {
#             'id': {'read_only': True}
#         }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","movie"]







