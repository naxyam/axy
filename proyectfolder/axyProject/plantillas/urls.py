from django.urls import path
from plantillas import views


urlpatterns = [   
    
    path('plantillas/adminPlantillas', views.plantillas, name='Plantillas'),
    path('plantillas/adminFicha', views.fichaSocReg.as_view(), name='FichaSocRegistro'),
    path('plantillas/adminFicha2', views.fichaSocReg2, name='FichaSocRegistro2'),
]
