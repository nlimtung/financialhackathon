# Generated by Django 4.0.1 on 2022-03-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_habit_profile_delete_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='businesscollector/'),
        ),
    ]