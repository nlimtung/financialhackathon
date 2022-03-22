from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name = 'home'),
    path('accounts/signup/', views.signup, name='signup'),
    path ('habit/create/', views.HabitCreate.as_view(), name = 'habit_create')

] 