# Generated by Django 3.2.8 on 2021-10-10 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinefood', '0006_alter_restaurantreview_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantreview',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='date',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='restaurantreview',
            name='user',
        ),
    ]
