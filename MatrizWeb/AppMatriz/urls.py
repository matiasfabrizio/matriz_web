from django.urls import path
from AppMatriz import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros', views.nosotros, name="Nosotros"),

    path('refuerzo_up/', views.refuerzo_up, name="RefuerzoUP"),
    path('refuerzo_up/nive-matematica', views.nive_mate, name="NiveMate"),
    path('refuerzo_up/matematicas1', views.mate1, name="Mate1"),
    path('refuerzo_up/matematicas2', views.mate2, name="Mate2"),
    path('refuerzo_up/matematicas-negocios', views.mate_nego, name="MateNego"),
    path('refuerzo_up/matematicas3', views.mate3, name="Mate3"),
    path('refuerzo_up/estadistica1', views.r_esta1, name="Esta1"),
    path('refuerzo_up/estadistica2', views.r_esta2, name="Esta2"),
    path('refuerzo_up/amn', views.amn, name="AMN"),
    path('refuerzo_up/nive-informatica', views.nive_info, name="NiveInfo"),
    path('refuerzo_up/analis-negocios', views.analisis, name="Analisis"),
    path('refuerzo_up/economia1', views.eco1, name="Eco1"),
    path('refuerzo_up/economia2', views.eco2, name="Eco2"),
    path('refuerzo_up/fundamentos-finanzas', views.funda_finanzas, name="FundaFinanzas"),
    path('refuerzo_up/nive-lenguaje', views.nive_lengua, name="NiveLengua"),
    path('refuerzo_up/lenguaje1', views.lengua1, name="Lengua1"),
    path('refuerzo_up/lenguaje2', views.lengua2, name="Lengua2"),

    path('refuerzo_pre/', views.refuerzo_pre, name="RefuerzoPre"),
    path('admision/', views.adm_up, name="AdmisionUP"),
    path('admision/regular', views.adm_regular, name="AdmisionRegular"),
    path('admision/selectiva', views.adm_selectiva, name="AdmisionSelectiva"),
    path('nivelacion/', views.nivelacion, name="Nivelacion"),
    path('adelanto/', views.adelanto, name="Adelanto"),
]
