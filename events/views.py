from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def eventshome(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'events.html', context)

def eventsingle(request, slug):
    post = Event.objects.filter(slug = slug).first()
    context = {'post':post}
    return render(request, 'post.html', context)
