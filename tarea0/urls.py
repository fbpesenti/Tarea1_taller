from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='tarea-home'),
    path('breaking-bad/<i>', views.breaking, name='tarea-breaking'),
    path('bettercallsaul/<season>', views.better, name='tarea-better'),
    path('episode/<episode>', views.episode, name='tarea-episode'),
]
