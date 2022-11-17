
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
# from .serializers import ArticleListSerializer, ArticleSerializer
from .serializers import CommunityListSerializer, CommunitySerializer
from .serializers import FoodsListSerializer, FoodsSerializer
# from .serializers import CommentSerializer
from .models import Community, CommunityTag, Foods
# from .models import Article
# from .models import Comment



# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def article_list(request):
#     if request.method == 'GET':
#         # articles = Article.objects.all()
#         articles = get_list_or_404(Article)
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # serializer.save()
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'DELETE', 'PUT'])
# def article_detail(request, article_pk):
#     # article = Article.objects.get(pk=article_pk)
#     article = get_object_or_404(Article, pk=article_pk)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         print(serializer.data)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

@api_view(['GET', 'POST'])
def community_list(request):
    if request.method == 'GET':
        community = Community.objects.all()
        # community = get_list_or_404(Community)
        serializer = CommunityListSerializer(community, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        tags_list = request.data['tags'].split('#')
        tags_pk_list = []
        for tag in tags_list:
            t, _ = CommunityTag.objects.get_or_create(name=tag)
            community = Community.objects.create()
            tags_pk_list.append(str(t.pk))
        print(tags_pk_list)
        print(request.data['tags'])
        request.data['tags'] = tags_pk_list
        # tags내용이 없으면 넣는다, 아니면 2번째값으로 false반환하지만 현재에는 의미가 없으므로 둘다 빈값
        serializer = CommunitySerializer(data=request.data)
        # print(serializer)
        # print(request.data)
        # print(request.data['tags'])          
        
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def community_detail(request, community_pk):
    # article = Article.objects.get(pk=article_pk)
    community = get_object_or_404(Community, pk=community_pk)

    if request.method == 'GET':
        serializer = CommunitySerializer(community)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def food_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        foods = get_list_or_404(Foods)
        serializer = FoodsListSerializer(foods, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FoodsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def food_detail(request, food_pk):
    # article = Article.objects.get(pk=article_pk)
    foods = get_object_or_404(Foods, pk=food_pk)

    if request.method == 'GET':
        serializer = FoodsSerializer(foods)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        foods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = FoodsSerializer(foods, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




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
