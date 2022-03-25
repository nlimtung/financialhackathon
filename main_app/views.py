from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Profile
from .models import Habit
from .models import User
import uuid
import boto3
import random

S3_BASE_URL = 'http://s3.ca-central-1.amazonaws.com/'
BUCKET = 'businesscollector'

@login_required
def home (request):
    return redirect  ('habits/index') 

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile_create')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class HabitCreate(LoginRequiredMixin, CreateView):
  model = Habit
  fields = ['habit_item', 'habit_cost', 'item', 'item_cost', 'goal_image']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    form.instance.initial_item_cost = form.instance.item_cost
    return super().form_valid(form)
  success_url = '/habits/index'

class ProfileCreate(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['name', 'lastname', 'email', 'profile_image']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)
  success_url = '/habits/index'

class HabitDelete(LoginRequiredMixin, DeleteView):
  model = Habit
  success_url='/habits/index/'

@login_required
def habits_index(request):
  habits = Habit.objects.filter( user = request.user).filter(completed_goal=False)
  return render(request, 'habits/index.html', { 'habits': habits })

@login_required
def habits_detail(request, habit_id):
  habit = Habit.objects.get(id=habit_id)
  return render(request, 'habits/detail.html', { 'habit': habit})

@login_required
def habits_update (request, pk):


  messages=['Be kind to yourself.',
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



  purchase_query =  Habit.objects.filter(pk= pk).values('item_cost')
  purchase_cost = (purchase_query[0]['item_cost'])
  habit_query =  Habit.objects.filter(pk= pk).values('habit_cost')
  habit_cost = (habit_query[0]['habit_cost'])

  

  new_cost = purchase_cost - habit_cost
  habit = Habit.objects.get(pk=pk)
  previous_saved_amount = habit.total_saved
  new_saved_amount = previous_saved_amount + habit_cost
  

  random_message = (random.choice(messages))
  print(random_message)

  badgepercent =  new_cost/habit.initial_item_cost
    
  if new_cost <= 0:
    habit.item_cost = 0
    habit.completed_goal = True
    habit.save()
  else:
    habit.item_cost = new_cost
    habit.total_saved = new_saved_amount
    habit.click_count = habit.click_count + 1 
    habit.random_message = random_message
    print(habit.click_count)

    habit.save()

  #90% complete
  if badgepercent <=.10:
    habit.ninety_goal = True
    habit.save()

  #80% complete
  if badgepercent <=.20:
    habit.eighty_goal = True
    habit.save()
  
  # 3 quarter badge
  if badgepercent <=0.75:
    habit.quarter_goal = True
    habit.save()

  #70% complete
  if badgepercent <=.30:
    habit.seventy_goal = True
    habit.save()

  #60% complete
  if badgepercent <=.40:
    habit.sixty_goal = True
    habit.save()

  # half badge
  if badgepercent <=0.5:
    habit.half_goal = True
    habit.save()

  #40% complete
  if badgepercent <=.60:
    habit.forty_goal = True
    habit.save()

  #30% complete
  if badgepercent <=.70:
    habit.thirty_goal = True
    habit.save()

  # quarter mark
  if badgepercent <=0.25:
    habit.three_quarter_goal = True
    habit.save()

  #20% complete
  if badgepercent <=.80:
    habit.twenty_goal = True
    habit.save()

  #10% complete
  if badgepercent <=.90:
    habit.ten_goal = True
    habit.save()
  return HttpResponseRedirect(reverse('detail', args=[str(pk)]), {"random_message":random_message})

@login_required
def profile (request):
  user = request.user
  profiles = Profile.objects.filter( user = request.user)
  return render  (request, "habits/profile.html", {"user" : user, 'profiles':profiles})  

class ProfileUpdate(LoginRequiredMixin,UpdateView):
  model = Profile
  fields = ['name', 'lastname', 'email', 'profile_image'] 
  success_url = '/habits/index'

@login_required
def completed(request):
  completed_habits = Habit.objects.filter( user = request.user).filter(completed_goal=True)
  return render(request, 'habits/completed.html', { 'completed_habits': completed_habits})




