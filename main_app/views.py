from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, DeleteView
from .models import Habit


def home (request):
    return render  (request, "home.html") 

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
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
    return super().form_valid(form)
  success_url = '/habits/index'

class HabitDelete(LoginRequiredMixin, DeleteView):
  model = Habit
  success_url='/habits/index/'

def habits_index(request):
  habits = Habit.objects.all()
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
  habit.item_cost = new_cost
  habit.save()

  return render(request, 'habits/detail.html', { 'habit': habit})



  
  # 
# we want to get the option by it's id 
# 
# we want to optain the average cost of the habit
# we want to optain the cost of the item
# onclick (form?) we minus the price of the habit from the price of the item
# we want to save the new cost of the item


