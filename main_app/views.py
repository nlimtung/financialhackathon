from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic.edit import CreateView, DeleteView
from .models import Habit
from .models import User
import uuid
import boto3
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
      return redirect('index')
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
  purchase_query =  Habit.objects.filter(pk= pk).values('item_cost')
  purchase_cost = (purchase_query[0]['item_cost'])
  habit_query =  Habit.objects.filter(pk= pk).values('habit_cost')
  habit_cost = (habit_query[0]['habit_cost'])

  new_cost = purchase_cost - habit_cost
  habit = Habit.objects.get(pk=pk)

  badgepercent =  new_cost/habit.initial_item_cost
  
  # quarter mark
  if badgepercent <=0.25:
    habit.quarter_goal = True
    habit.save()

  # half badge
  if badgepercent <=0.5:
    habit.half_goal = True
    habit.save()
  
  # 3 quarter badge
  if badgepercent <=0.75:
    habit.three_quarter_goal = True
    habit.save()
  
  # completed 
    if new_cost <= 0:
      habit.item_cost = 0
      habit.completed_goal = True
      habit.save()
    else:
      habit.item_cost = new_cost
      habit.save()
  
  return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

@login_required
def profile (request):
  user = request.user
  address = request.user.email
  return render  (request, "habits/profile.html", {"user" : user})  

@login_required
def completed(request):
  completed_habits = Habit.objects.filter( user = request.user).filter(completed_goal=True)
  return render(request, 'habits/completed.html', { 'completed_habits': completed_habits})




