from re import sub
from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, Gallery, Contact, Recruitment_Query
from research.models import Research
from events.models import Event
from django.contrib import messages
from blog.models import Post


def index(request):
    research = Research.objects.all()[:3]
    posts = Post.objects.all()[:3]
    events  = Event.objects.all()[:3]
    gallery = Gallery.objects.all()
    context = {'research':research, 'posts':posts, 'events':events, 'gallery':gallery}
    return render(request, 'home.html', context)

def about(request):
    team = Team.objects.all()
    context = {'team':team}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        newcontact = Contact(name = name, email = email, subject = subject, message = message)
        newcontact.save()
        messages.success(request, 'Message Sent! The TARS Mail Man Is On the Way :)')
    return render(request, 'contact.html')

def recruitment(request):
    if request.method == "POST":
        name = request.POST['name']
        collegeid = request.POST['collegeid']
        branch = request.POST['branch']
        whatsapp = request.POST['whatsapp']
        proposal = request.POST['proposal']

        newproposal = Recruitment_Query(name = name, college_id = collegeid, branch = branch, whatsapp = whatsapp, proposal = proposal)
        newproposal.save()
        messages.success(request, 'Message Sent! The TARS Mail Man Is On the Way :)')
    return render(request, 'recruitment.html')

def team(request):
    team = Team.objects.filter(is_core  = True)
    not_core = Team.objects.filter(is_core  = False)
    context = {'team':team, 'not_core': not_core}
    return render(request, 'team.html', context)