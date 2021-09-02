from django.urls import path
from plantillas import views


urlpatterns = [   
    
    path('plantillas/adminPlantillas', views.beneListView.as_view(), name='Plantillas'),
    path('plantillas/adminFicha', views.fichaSocReg.as_view(), name='FichaSocRegistro'),
    path('plantillas/adminPlantillas/invoice/pdf/<int:pk>', views.fisorePdfView.as_view(), name='fisorePdf'),
  
  
    #path('plantillas/adminFicha2', views.fichaSocReg2, name='FichaSocRegistro2'),
    
]
