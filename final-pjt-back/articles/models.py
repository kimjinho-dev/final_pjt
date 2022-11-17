from django.db import models
from django.conf import settings

# from django.contrib.postgres.fields import ArrayField

class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # user 모델과 1:N 매칭
    title = models.CharField(max_length=100)                                        # 제목
    content = models.TextField()                                                    # 내용
    created_at = models.DateTimeField(auto_now_add=True)                            # 작성시간
    updated_at = models.DateTimeField(auto_now=True)                                # 업데이트 시간(수정기는 없으면 불필요)
    # tags = models.TextField(null=True)                                                       # 태그(문자열로 join 구분자 ',' 사용예정)
    tags = models.ManyToManyField('CommunityTag', related_name='community', blank=True,)
    image_id = models.TextField(null=True)                                                   # 저장된 사진 id
    # tags = ArrayField(models.CharField(max_length=20), blank=True)

class CommunityTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = 'tags'

class Foods(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tags = models.TextField(null=True)
    tags = models.ManyToManyField('FoodTag', related_name='tag')
    image_id = models.TextField(null=True)

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class CommunityTag(models.Model):
#     text = models.TextField(max_length=20)
    
class FoodTag(models.Model):
    name = models.CharField(max_length=100)
