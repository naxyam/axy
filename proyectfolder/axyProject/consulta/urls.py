from django.urls import path
from consulta import views


urlpatterns = [
    
  
    path('adminListar', views.beneListView.as_view(), name='Listar'),
    path('plantillas/adminFicha/<int:pk>/', views.beneUpdateView.as_view(), name='Update'),
    path('plantillas/delete/<int:pk>/', views.beneDeleteView.as_view(), name='Delete'),
   

]