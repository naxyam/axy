
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from plantillas.forms import formFichaReg


def plantillas(request):   
    return render(request, 'plantillas/adminPlantillas.html')


def fichaSocReg2(request):   
    return render(request, 'adminFicha2.html')


class fichaSocReg(CreateView):
    form_class = formFichaReg
    template_name = 'plantillas/adminFicha.html'  

    def form_valid(self, form):
        beneficiario = form['formFichaReg'].save(commit=False)
        beneficiario.save()
        return HttpResponseRedirect(reverse('plantillas/adminFicha2'))

class SuccessView(TemplateView):
    template_name = 'plantillas/adminFicha2.html'

''''

if request.method=='POST':
  form = ProfileForm(request.POST)
  if form.is_valid():
    profile = form.save(commit=False)
    profile.user = request.user
    profile.save()
else:
  form = ProfileForm()

return render_to_response(template_name, {"profile_form": form}, context_instance=RequestContext(request))

'''
        
  

            




