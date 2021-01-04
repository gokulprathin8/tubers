from django.shortcuts import render
from youtubers.models import Youtuber
from . import models

def home(request):
    sliders = models.Slider.objects.all()
    teams  = models.Team.objects.all()
    youtuber = Youtuber.objects.order_by("-created_at").filter(is_featured=True)
    data = {
        'sliders': sliders,
        'teams': teams,
        'youtuber': youtuber,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')