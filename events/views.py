from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def eventshome(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'events.html', context)
