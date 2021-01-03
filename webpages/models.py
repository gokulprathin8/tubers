from django.db import models

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    buttom_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/%m/%d/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.URLField()
    insta_link = models.URLField()
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name