
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, View
from plantillas.forms import formFichaReg
from plantillas.models import Beneficiario
from django.http import HttpResponse
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class beneListView(ListView):
    model= Beneficiario
    template_name= 'plantillas/adminPlantillas.html'

        

class fichaSocReg(CreateView): 
    model=Beneficiario
    form_class = formFichaReg
    template_name = 'plantillas/adminFicha.html' 
    success_url = reverse_lazy('Plantillas')


class fisorePdfView(View):
    def get(self, request, *args, **kwargs): 
        try:       
            template = get_template('plantillas/invoice.html')
            context = {'title': 'Mi primer pdf'}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponse('Tenemos errores' + html + '</pre>')
            return response
        except:
            pass
            return HttpResponseRedirect(reverse_lazy('Plantillas'))


    
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
        
  

            




