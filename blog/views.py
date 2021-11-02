from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def bloghome(request):
    posts = Post.objects.all()
    context = {'posts' : posts} 
    return render(request, 'blog.html', context)
