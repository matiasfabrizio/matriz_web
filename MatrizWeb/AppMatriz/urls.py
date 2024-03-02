from django.urls import path
from AppMatriz import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('admision/', views.admision, name="Admision"),
    path('adelanto/', views.adelanto, name="Adelanto"),
    path('nivelacion/', views.nivelacion, name="Nivelacion"),
    path('refuerzo/', views.refuerzo2, name="Refuerzo"),
    path('refuerzo/estadistica1', views.r_esta1, name="Esta1"),
    path('refuerzo/estadistica2', views.r_esta2, name="Esta2"),
    path('refuerzopre/', views.refuerzopre, name="RefuerzoPre"),
]
