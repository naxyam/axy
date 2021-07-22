from django.urls import path
from axyProyectApp import views

urlpatterns = [
    
    path('', views.index, name='Index'),
    path('quienesomos', views.quienesomos, name='Quienesomos'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),
    path('axy', views.login, name='Login')

]