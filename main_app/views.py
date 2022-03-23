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

class HabitCreate(CreateView):
  model = Habit
  fields = ['habit_item', 'habit_cost', 'item', 'item_cost']
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
  habits = Habit.objects.filter( user = request.user)
  return render(request, 'habits/index.html', { 'habits': habits })

def habits_detail(request, habit_id):
  habit = Habit.objects.get(id=habit_id)
  return render(request, 'habits/detail.html', { 'habit': habit})

def habits_update (request, pk):
  purchase_query =  Habit.objects.filter(pk= pk).values('item_cost')
  purchase_cost = (purchase_query[0]['item_cost'])
  habit_query =  Habit.objects.filter(pk= pk).values('habit_cost')
  habit_cost = (habit_query[0]['habit_cost'])

  new_cost = purchase_cost - habit_cost
  habit = Habit.objects.get(pk=pk)

  if new_cost < 0:
    habit.item_cost = 0
    habit.completed_goal = True
    habit.save()
  else:
    habit.item_cost = new_cost
    habit.save()
 

  return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

  # return render(request, 'habits/detail.html', { 'habit': habit})

#change habit to profile later****
def profile (request):
  user = request.user
  address = request.user.email

  

  return render  (request, "habits/profile.html", {"user" : user})  

def completed(request):
  completed_habits = Habit.objects.filter( user = request.user).filter(completed_goal=True)
  return render(request, 'habits/completed.html', { 'completed_habits': completed_habits})




