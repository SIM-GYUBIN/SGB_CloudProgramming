import os.path

from django.contrib.auth.models import User
from django.db import models
from markdown import markdown
from markdownx.models import MarkdownxField



class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    #새로운거 추가됐을때 넣어라, 시간 오토로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #작성자는 필수로 있어야 하니 on_delete로, 콜백함수넘기는 거니 cascade 뒤에 ()없이
    #cascade 대신 다른 여러 선택지들 많음, 막 어떤 다른 유저로 변경된다던지
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return f'[{self.pk}]{self.title} - {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_content_markdown(self):
        return markdown(self.content);

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'