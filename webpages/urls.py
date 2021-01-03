from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.about, name="services"),
    path('contact/', views.about, name="contact"),
]