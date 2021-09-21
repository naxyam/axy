from django.shortcuts import render
from django.views.generic import ListView
from plantillas.models import Beneficiario

class beneListView(ListView):
    model= Beneficiario
    template_name= 'consulta/adminListar.html'
