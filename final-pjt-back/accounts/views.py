from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer
from .models import User

from articles.serializers import CommunityListSerializer


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def user_post(request, username):
    user_post = get_object_or_404(User, username=username).community_set.all()
    serializer = CommunityListSerializer(user_post, many=True)
    return Response(serializer.data)


    