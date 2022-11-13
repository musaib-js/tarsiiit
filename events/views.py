from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Registration
from django.contrib import messages

def eventshome(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'events.html', context)

def eventsingle(request, slug):
    post = Event.objects.filter(slug = slug).first()
    print(post)
    context = {'post':post}
    return render(request, 'eventsingle.html', context)

def eventregister(request):
    event = Event.objects.filter(registrations_open = True)
    context = {'event': event}

    if request.method == 'POST':
        event = request.POST['event']
        name = request.POST['name']
        id_no = request.POST['id']
        branch = request.POST['branch']
        batch = request.POST['batch']

        newregistration = Registration(event = event, name = name, id_no = id_no, branch  = branch, batch = batch)
        newregistration.save()
        messages.success(request, 'Registration Successfull. See you in the event :)')
    return render(request, 'register.html', context)
