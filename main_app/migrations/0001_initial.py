# Generated by Django 4.0.1 on 2022-03-24 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit_item', models.CharField(max_length=50, verbose_name='HABIT NAME')),
                ('habit_cost', models.FloatField(verbose_name='ESTIMATED COST')),
                ('item', models.CharField(max_length=50, verbose_name='NAME')),
                ('item_cost', models.FloatField(verbose_name='ITEM COST')),
                ('initial_item_cost', models.FloatField(null=True, verbose_name='initial cost')),
                ('total_saved', models.FloatField(default=0, verbose_name='total saved')),
                ('click_count', models.IntegerField(default=0, verbose_name='click count')),
                ('random_message', models.CharField(max_length=220)),
                ('completed_goal', models.BooleanField(default=False)),
                ('ninety_goal', models.BooleanField(default=False)),
                ('eighty_goal', models.BooleanField(default=False)),
                ('seventy_goal', models.BooleanField(default=False)),
                ('sixty_goal', models.BooleanField(default=False)),
                ('forty_goal', models.BooleanField(default=False)),
                ('thirty_goal', models.BooleanField(default=False)),
                ('twenty_goal', models.BooleanField(default=False)),
                ('ten_goal', models.BooleanField(default=False)),
                ('half_goal', models.BooleanField(default=False)),
                ('quarter_goal', models.BooleanField(default=False)),
                ('three_quarter_goal', models.BooleanField(default=False)),
                ('goal_image', models.ImageField(default='default.png', null=True, upload_to='businesscollector/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
