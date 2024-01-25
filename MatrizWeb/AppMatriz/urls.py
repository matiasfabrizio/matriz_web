from django.urls import path
from AppMatriz import views

urlpatterns = [
    path('', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
]