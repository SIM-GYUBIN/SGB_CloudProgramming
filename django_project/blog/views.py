from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


# 풀 경로로 import하면 문제 생김

def index(request) :
    # 사용자의 요청을 받아 이런저런일을 여기서
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context


def categories_page(request, slug):
    if slug == 'no-category':
        category = '미분류'
        # 위 코드 카테고리 없는애들 필터링해서 찾아옴
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)


    context = {
        'category': category,
        'categories': Category.objects.all(),
        'post_list': post_list,
        'no_category_count' : Post.objects.filter(category=None).count()
    }
    return render(request, 'blog/post_list.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    #이 태그에 해당하는 것들 보여줘라 하는 것
    post_list = tag.post_set.all()

    context = {
        'tag': tag,
        'categories': Category.objects.all(),
        'post_list': post_list,
        'no_category_count': Post.objects.filter(category=None).count()
    }
    return render(request, 'blog/post_list.html', context)