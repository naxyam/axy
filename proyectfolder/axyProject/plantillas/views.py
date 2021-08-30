
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from plantillas.forms import formFichaReg
from plantillas.models import Beneficiario
from django.http import HttpResponseRedirect



def plantillas(request):   
    return render(request, 'plantillas/adminPlantillas.html')

        
def success(request):   
    return render(request, 'plantillas/success.html')

class fichaSocReg(CreateView): 
    model=Beneficiario
    form_class = formFichaReg
    template_name = 'plantillas/adminFicha.html' 
    success_url = reverse_lazy('success')
    
''' 
def post(self, request, ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        # <process form cleaned data>
            return HttpResponseRedirect(success) '''
        








''''
def fichaSocReg2(request):   
    return render(request, 'plantillas/adminFicha2.html')
'''





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
        
  

            




