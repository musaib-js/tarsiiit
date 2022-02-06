from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def bloghome(request):
    posts = Post.objects.all()
    fposts = Post.objects.filter(is_featured = True)
    context = {'posts' : posts, 'fposts':fposts} 
    return render(request, 'blog.html', context)
