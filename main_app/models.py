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


def random_message():
  random_message=['Be kind to yourself.',
  'You can do hard things.',
  'Remember your why.',
  'You’re doing exactly what you should be doing. Hang in there.',
  'A journey starts with one step.',
  'Don’t let how you feel make you forget what you deserve.',
  '“It always seems impossible until it is done.” — Nelson Mandela',
  'Just wanted to send you a smile today. :)',
  'You’re being so strong—and patient. Keep the faith. Things are going to start looking up soon.',
  'Make today matter!',
  'You should be so proud of yourself.',
  'It may not be easy, but it will be worth it!',
  'I can’t wait to see what you do next.',
  'Success doesn’t come from what you do occasionally. It comes from what you do consistently.',
  'When the world says, “Give up,” Hope whispers, “Try it one more time.”',
  'Every day may not be a good day, but there is something good in every day.',
  'Today’s a good day to have a great day.',
  'Today will never come again. Look forward to tomorrow.',
  'Your speed doesn’t matter. Forward is forward.',
  'A positive mind finds opportunity in everything.',
  'You are stronger than you think you are.',
  'Don’t forget to be awesome.',
  'Progress, not perfection.',
  'The best view comes after the hardest climb.',
  'You are capable of more than you know.',
  'If you never try, you’ll never know.',
  'Don’t try to be perfect. Just try to be better than you were yesterday.',
  'This totally sucks, but you totally don’t suck!',
  'I believe in you! And unicorns. But mostly you.',
  'If it was easy, everyone would do it.',
  'Small progress is still progress.',
  'Remember why you started.',
  'Keep going until you are proud.',
  'Be positive, patient, and persistent.',
  '“Don’t let your dreams be dreams.” — Jack Johnson']





