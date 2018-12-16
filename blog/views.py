from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown
import datetime

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    context = {
        'post_list': post_list

    }
    return render(request,'blog/index.html',context)
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.post_body = markdown.markdown(post.post_body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})

def archives(request, year, month):

    dayMax = 30
    months = [1, 3, 5, 7, 8, 10, 12]
    if int(month) in months:
        dayMax = 31
    post_list = Post.objects.filter(
        created_time__range=(datetime.date(int(year), int(month), 1),
                             datetime.date(int(year), int(month), dayMax)
                             )).order_by('-created_time')

    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})