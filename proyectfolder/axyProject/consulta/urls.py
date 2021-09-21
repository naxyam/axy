from django.urls import path
from consulta.views import beneListView


urlpatterns = [
    
  
    path('adminListar', beneListView.as_view(), name='Listar'),
   

]