from django.urls import path
from panelPrincipal import views




urlpatterns = [   
    
    path('', views.panelPrincipal, name='PanelPrincipal'),
    path('adminNuevoDocumento', views.nuevodocumento, name='NuevoDocumento'),
]