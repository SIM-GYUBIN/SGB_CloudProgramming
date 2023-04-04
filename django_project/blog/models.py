import os.path

from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    #새로운거 추가됐을때 넣어라, 시간 오토로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #작성자는 필수로 있어야 하니 on_delete로, 콜백함수넘기는 거니 cascade 뒤에 ()없이
    #cascade 대신 다른 여러 선택지들 많음, 막 어떤 다른 유저로 변경된다던지
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
