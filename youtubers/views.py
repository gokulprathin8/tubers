from django.shortcuts import render, get_object_or_404
from . import models

def youtubers(request):
    tubers = models.Youtuber.objects.order_by('-created_at')
    data = {
        'tubers': tubers
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_details(request, id):
    tuber = get_object_or_404(models.Youtuber, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtubers_detail.html', data)

def search(request):
    tubers = models.Youtuber.objects.all()
    city_search = models.Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = models.Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = models.Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(city__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(city__iexact=category)

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_search,
        'category_search': category_search,
    }
    return render(request, 'youtubers/search.html', data)