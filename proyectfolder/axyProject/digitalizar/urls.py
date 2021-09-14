from django.urls import path
from . import views


urlpatterns = [
    
  
    path('digitalizar', views.digitalizar, name='Digitalizar'),
   

]
