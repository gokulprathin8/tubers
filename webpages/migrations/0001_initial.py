# Generated by Django 3.1.4 on 2021-01-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('buttom_text', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/slider/%Y/%m/%d/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
