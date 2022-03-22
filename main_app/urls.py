from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name = 'home'),
    path('accounts/signup/', views.signup, name='signup'),
    path ('habits/create/', views.HabitCreate.as_view(), name = 'habit_create'),
    path('habits/<int:habit_id>/', views.habits_detail, name='detail'),
    path('habits/index/', views.habits_index, name='index'),
    path('habits/<int:pk>/delete/', views.HabitDelete.as_view(), name='habit_delete'),
    path('habits/<int:pk>/update/', views.habits_update, name='habit_update'),

] 