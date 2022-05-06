from django.shortcuts import redirect, render
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.dates import BaseMonthArchiveView
from plantillas.models import Beneficiario, Historiaclinica
from plantillas.forms import formFichaReg, formHistClinica
from django.urls import reverse_lazy

class beneListView(ListView):
    model= Beneficiario
    template_name= 'consulta/adminListar.html'


class beneUpdateView(UpdateView):
    model= Beneficiario
    form_class= formFichaReg
    template_name= 'plantillas/adminFicha.html'
    success_url= reverse_lazy('success')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Edicion de un beneficiario'
        context['entity']= 'Beneficiario'
        context['list_url']= reverse_lazy('Listar')
        context['action']= 'edit'
        return context
    
    

'''
def categoria(request, categoria_id):
	categoria=Categoria.objects.get(id=categoria_id)
	posts=Post.objects.filter(Categorias=categoria)
	return render(request,'blog/categoria.html',{'categoria':categoria,'posts': posts})
        
'''


def HistClinicaUpdate(request, benef_id):  
    beneficiario = Beneficiario.objects.get(id=benef_id)
    hisclinica = Historiaclinica.objects.filter(id = beneficiario)
    if request.method == "GET":
        form = formFichaReginstance =(hisclinica)
    else:
        form = formFichaReg(request.POST, instance=hisclinica)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('success'))



class beneDeleteView(DeleteView):
    model= Beneficiario
    template_name = 'plantillas/delete.html'
    success_url = reverse_lazy('Listar')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Eliminación de un beneficiario'
        context['entity']= 'Beneficiario'              
        return context


