from django.urls import path
from consulta import views


urlpatterns = [
    
  
    path('adminListar', views.beneListView.as_view(), name='Listar'),
    path('plantillas/adminFicha/<str:pk>/', views.beneUpdateView.as_view(), name='Update'),
    path('plantillas/delete/<int:pk>/', views.beneDeleteView.as_view(), name='Delete'),
    path('plantillas/HistClinicaUpdate/<int:pk>/', views.HistClinicaUpdate, name='UpdateHistClinica'),
    path('plantillas/success/', views.HistclinicaUpdateView, name='success'),

   

]