from django.shortcuts import render
from .models import Posts


def index(request):
    return render(request,'index.html')

def blog(request):
    posts = Posts.objects.all()[0:10]
    context = {
        'posts':posts
    }
    return render(request,'post.html', context)
