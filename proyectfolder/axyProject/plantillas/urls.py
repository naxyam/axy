from django.urls import path
from plantillas import views


urlpatterns = [   
    
 
    path('plantillas/adminFicha', views.fichaSocReg.as_view(), name='FichaSocRegistro'),
    path('plantillas/adminPlantillas/invoice/pdf/<int:pk>', views.fisorePdfView.as_view(), name='fisorePdf'),
    path('plantillas/success', views.exito, name='exito'),
    path('plantillas/adminFicha2', views.histClinica.as_view(), name='HistClinica'),
  
  
    #path('plantillas/adminFicha2', views.fichaSocReg2, name='FichaSocRegistro2'),
    
]
