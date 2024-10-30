from django.contrib import admin
from .models import Color, Profile, Category, Task, Subtask, TaskHistory

admin.site.register(Color)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(TaskHistory)

# Register your models here.
