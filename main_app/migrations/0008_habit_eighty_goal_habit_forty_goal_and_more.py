# Generated by Django 4.0.1 on 2022-03-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_habit_badgepercent_habit_ninety_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='eighty_goal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='forty_goal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='seventy_goal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='sixty_goal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='ten_goal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='thirty_goal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='twenty_goal',
            field=models.BooleanField(default=False),
        ),
    ]
