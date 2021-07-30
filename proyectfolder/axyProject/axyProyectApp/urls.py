from django.urls import path
from axyProyectApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='Index'),
    path('quienesomos', views.quienesomos, name='Quienesomos'),
    path('axy', views.login, name='Login')

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)