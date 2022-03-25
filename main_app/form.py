from django.forms import ModelForm
from .models import Habit 
from django import forms


class HabitForm(ModelForm):
    class Meta:
        model = Widget 
        fields = ['habit_item', 'habit_cost', 'item', 'item_cost', 'goal_image']
