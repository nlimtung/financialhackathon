from django.contrib import admin
from .models import Habit
from .models import Profile


# Register your models here.
admin.site.register(Habit)
admin.site.register(Profile)
