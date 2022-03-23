from unicodedata import decimal
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Habit (models.Model):
    habit_item = models.CharField(verbose_name=u"HABIT NAME", max_length = 50, )
    habit_cost = models.FloatField("ESTIMATED COST")
    item = models.CharField(verbose_name=u"NAME", max_length = 50)
    item_cost = models.FloatField("ITEM COST")
    initial_item_cost = models.FloatField("initial cost", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed_goal = models.BooleanField(default= False)
    half_goal =  models.BooleanField(default= False)
    quarter_goal = models.BooleanField(default= False)
    three_quarter_goal = models.BooleanField(default= False)
    goal_image = models.ImageField(upload_to='businesscollector/',default='default.png',null=True)

    def __str__(self):
        return self.item
    def get_absolute_url(self):
        return reverse('detail', kwargs={'habit_id': self.id})




