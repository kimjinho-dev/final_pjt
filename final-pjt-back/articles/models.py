from django.db import models
from django.conf import settings

class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # user 모델과 1:N 매칭
    title = models.CharField(max_length=100)                                        # 제목
    content = models.TextField()                                                    # 내용
    created_at = models.DateTimeField(auto_now_add=True)                            # 작성시간
    updated_at = models.DateTimeField(auto_now=True)                                # 업데이트 시간(수정기는 없으면 불필요)
    tags = models.ManyToManyField('CommunityTag', related_name='community', blank=True,)
    image_id = models.TextField(null=True)                                                   # 저장된 사진 id
    
class CommunityTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    
