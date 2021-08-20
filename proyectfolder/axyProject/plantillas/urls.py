from django.urls import path
from . import views


urlpatterns = [   
    
    
    path('plantilla/adminFicha', views.getFicha.as_view(), name='FichaSocRegistro'),
]
