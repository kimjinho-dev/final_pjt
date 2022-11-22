from django.db import models
from django.conf import settings

# def image_directory_path(instance, filename):
#     return 'media/{0}/{1}'.format(instance.upload_user.username, filename)  # user를 upload_user로 저장했기 때문에 instance.upload_user로 사용함
# def image_path(instance):
#     return 'users/{0}'.format(instance.upload_user.username)

class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # user 모델과 1:N 매칭
    title = models.CharField(max_length=100)                                        # 제목
    content = models.TextField()                                                    # 내용
    created_at = models.DateTimeField(auto_now_add=True)                            # 작성시간
    updated_at = models.DateTimeField(auto_now=True)                                # 업데이트 시간(수정기는 없으면 불필요)
    tags = models.ManyToManyField('CommunityTag', related_name='community', blank=True,)
    image = models.ImageField(blank=True, upload_to='images', null=True)                                                   # 저장된 사진 id
    # base64 = models.TextField(blank=True)


class CommunityTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Profile(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # user 모델과 1:N 매칭
#     nickname = models.CharField(max_length=20)


#     def __str__(self):
#         return self.name
