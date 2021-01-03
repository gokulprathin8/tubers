from django.shortcuts import render
from . import models

def home(request):
    sliders = models.Slider.objects.all()
    teams  = models.Team.objects.all()
    data = {
        'sliders': sliders,
        'teams': teams
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')