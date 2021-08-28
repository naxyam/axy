
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, TemplateView
from plantillas.forms import formFichaReg
from plantillas.models import Beneficiario


def plantillas(request):   
    return render(request, 'plantillas/adminPlantillas.html')

class fichaSocReg(CreateView):
    model=Beneficiario
    form_class = formFichaReg
    template_name = 'plantillas/adminFicha.html' 
    success_url = reverse_lazy('plantillas: success') 

'''def fichaSocReg2(request):   
    return render(request, 'plantillas/adminFicha2.html')'''

def success(request):   
    return render(request, 'plantillas/success.html')



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
        
  

            




