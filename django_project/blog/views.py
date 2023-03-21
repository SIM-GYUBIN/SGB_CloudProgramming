from django.shortcuts import render

from .models import Post
# 풀 경로로 import하면 문제 생김

def index(request) :
    # 사용자의 요청을 받아 이런저런일을 여기서
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'blog/index.html',{
        'posts': posts,
    })