from django.urls import path
from AppMatriz import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('admision/', views.admision, name="Admision"),
    path('refuerzo/', views.refuerzo, name="Refuerzo"),
    path('refuerzo/<str:codigo_curso>/', views.refuerzo_cursos, name="Refuerzo Cursos"),
]