# Generated by Django 4.0.1 on 2022-03-25 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_habit_habit_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.png', null=True, upload_to='businesscollector/'),
        ),
    ]
