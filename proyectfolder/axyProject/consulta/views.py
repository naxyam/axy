from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.dates import BaseMonthArchiveView
from plantillas.models import Beneficiario
from plantillas.forms import formFichaReg
from django.urls import reverse_lazy

class beneListView(ListView):
    model= Beneficiario
    template_name= 'consulta/adminListar.html'


class beneUpdateView(UpdateView):
    model= Beneficiario
    form_class= formFichaReg
    template_name= 'plantillas/adminFicha.html'
    success_url= reverse_lazy('Listar')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Edicion de un beneficiario'
        context['entity']= 'Beneficiario'
        context['list_url']= reverse_lazy('Listar')
        context['action']= 'edit'
        return context

class beneDeleteView(DeleteView):
    model= Beneficiario
    template_name = 'plantillas/delete.html'
    success_url = reverse_lazy('Listar')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Eliminación de un beneficiario'
        context['entity']= 'Beneficiario'
              
        return context


