
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CommunityListSerializer, CommunitySerializer
from .models import Community, CommunityTag


@api_view(['GET', 'POST'])
def community_list(request):
    if request.method == 'GET':
        community = Community.objects.all()
        serializer = CommunityListSerializer(community, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        tags_list = request.POST.get('tags').split('#')
        # #으로 내용 구분. 추후에 공백제거처리
        community = Community.objects.create(
            user=request.user,
            title=request.POST.get('title',''),
            content=request.POST.get('content',''),
        )
        for tag in tags_list: 
            if tag:
                tag = tag.strip()
                t, _ = CommunityTag.objects.get_or_create(name=tag)
                # tags내용이 없으면 넣는다, 아니면 2번째값으로 false반환하지만 현재에는 의미가 없으므로 둘다 빈값
                community.tags.add(t)
                # tags 추가(m:m)        
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    if request.method == 'GET':
        serializer = CommunitySerializer(community)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # elif request.method == 'PUT':
    #     serializer = CommunitySerializer(community, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


# 댓글부분

# @api_view(['GET'])
# def comment_list(request):
#     if request.method == 'GET':
#         # comments = Comment.objects.all()
#         comments = get_list_or_404(Comment)
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)


# @api_view(['GET', 'DELETE', 'PUT'])
# def comment_detail(request, comment_pk):
#     # comment = Comment.objects.get(pk=comment_pk)
#     comment = get_object_or_404(Comment, pk=comment_pk)

#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
  


# @api_view(['POST'])
# def comment_create(request, article_pk):
#     # article = Article.objects.get(pk=article_pk)
#     article = get_object_or_404(Article, pk=article_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(article=article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
