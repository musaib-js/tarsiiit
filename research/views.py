from django.shortcuts import render
from django.http import HttpResponse
from .models import Research

def researchhome(request):
    featuredresearch = Research.objects.filter(is_featured = True)
    research = Research.objects.all()
    context = {'research' : research, 'fresearch':featuredresearch}  
    return render(request,  'research.html', context)
