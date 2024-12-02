
from ast import mod
from os import name
from django.db import models
from django.contrib.auth.models import User



class Color(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=7)  # Hex-Farbcode, z.B. #FFFFFF
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=2)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('done', 'Done'),
        ('awaiting_feedback', 'Awaiting Feedback'),
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    duedate = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name

class Subtask(models.Model):
    
    done = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.name
    
class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    change_description = models.TextField()

    def __str__(self):
        return f"{self.task.name} - {self.timestamp}"