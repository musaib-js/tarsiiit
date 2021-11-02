from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from research.models import Research
from events.models import Event
from blog.models import Post

def index(request):
    research = Research.objects.all()[:3]
    posts = Post.objects.all()[:3]
    events  = Event.objects.all()[:3]
    context = {'research':research, 'posts':posts, 'events':events}
    return render(request, 'index.html', context)

def about(request):
    team = Team.objects.all()
    context = {'team':team}
    return render(request, 'about.html', context)