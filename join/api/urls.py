from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProfileViewSet, TaskViewSet, SubtaskViewSet, UserViewSet, ColorViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'colors', ColorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]