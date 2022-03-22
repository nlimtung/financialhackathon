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
  success_url = '/'

class HabitDelete(LoginRequiredMixin, DeleteView):
  model = Habit
  success_url='/habits/index/'

def habits_index(request):
  habits = Habit.objects.all()
  return render(request, 'habits/index.html', { 'habits': habits })



