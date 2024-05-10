from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="Inicio"),
    path('nosotros', nosotros, name="Nosotros"),
    path('refuerzo_up/', refuerzo_up, name="RefuerzoUP"),
    path('refuerzo_up/nive-matematica', nive_mate, name="NiveMate"),
    path('refuerzo_up/matematicas1', mate1, name="Mate1"),
    path('refuerzo_up/matematicas2', mate2, name="Mate2"),
    path('refuerzo_up/matematicas-negocios', mate_nego, name="MateNego"),
    path('refuerzo_up/matematicas3', mate3, name="Mate3"),
    path('refuerzo_up/estadistica1', r_esta1, name="Esta1"),
    path('refuerzo_up/estadistica2', r_esta2, name="Esta2"),
    path('refuerzo_up/amn', amn, name="AMN"),
    path('refuerzo_up/nive-informatica', nive_info, name="NiveInfo"),
    path('refuerzo_up/analis-negocios', analisis, name="Analisis"),
    path('refuerzo_up/economia1', eco1, name="Eco1"),
    path('refuerzo_up/economia2', eco2, name="Eco2"),
    path('refuerzo_up/fundamentos-finanzas', funda_finanzas, name="FundaFinanzas"),
    path('refuerzo_up/nive-lenguaje', nive_lengua, name="NiveLengua"),
    path('refuerzo_up/lenguaje1', lengua1, name="Lengua1"),
    path('refuerzo_up/lenguaje2', lengua2, name="Lengua2"),
    path('refuerzo_pre/', refuerzo_pre, name="RefuerzoPre"),
    path('admision/', adm_up, name="AdmisionUP"),
    path('admision/regular', adm_regular, name="AdmisionRegular"),
    path('admision/selectiva', adm_selectiva, name="AdmisionSelectiva"),
    path('nivelacion/', nivelacion, name="Nivelacion"),
    path('adelanto/', adelanto, name="Adelanto"),
]

#Para las imágenes
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)