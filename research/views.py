from django.shortcuts import render
from django.http import HttpResponse
from .models import Research

def researchhome(request):
    research = Research.objects.all()
    context = {'research' : research}  
    return render(request,  'research.html', context)
