from django.urls import path
from . import views


urlpatterns = [   
    
    path('', views.plantillas, name='Plantillas'),
    path('adminFicha', views.fichaSocReg, name='FichaSocRegistro'),
    path('adminFicha2', views.fichaSocReg2, name='FichaSocRegistro2'),
]
