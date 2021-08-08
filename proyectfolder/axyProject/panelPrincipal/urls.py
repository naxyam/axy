from django.urls import path
from panelPrincipal import views
from django.conf import settings



urlpatterns = [   
    
    path('', views.panelPrincipal, name='PanelPrincipal'),
]