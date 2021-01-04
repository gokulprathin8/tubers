from django.db import models
from ckeditor import fields
from datetime import datetime

class Youtuber(models.Model):

    crew_choices = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    )

    camera_choices = (
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('red', 'red'),
        ('fuji', 'fuji'),
        ('other', 'other'),
    )

    category_choices = (
        ('code', 'code'),
        ('mobile_review', 'mobile_review'),
        ('vlogs', 'vlogs'),
        ('comdey', 'comedy'),
        ('gaming', 'gaming')
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%y/%m/%d')
    video_url = models.CharField(max_length=255)
    description = fields.RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    crew = models.CharField(max_length=255, choices=crew_choices)
    camera_type = models.CharField(max_length=255, choices=camera_choices)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=category_choices)
    is_featured = models.BooleanField()
    category = models.CharField(max_length=255, choices=category_choices)
    django_created_at = models.DateField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
