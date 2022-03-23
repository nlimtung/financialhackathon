from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Habit (models.Model):
    habit_item = models.CharField(max_length = 50)
    habit_cost = models.FloatField("habit cost")
    item = models.CharField(max_length = 50)
    item_cost = models.FloatField("cost")
    initial_item_cost = models.FloatField("initial cost", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed_goal = models.BooleanField(default= False)

    def __str__(self):
        return self.item
    def get_absolute_url(self):
        return reverse('detail', kwargs={'habit_id': self.id})



