
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView, View
from plantillas.forms import formFichaReg, formHistClinica
from plantillas.models import Beneficiario, Historiaclinica
from django.http import HttpResponse
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import date
born = Beneficiario.benef_fechanac

        

class fichaSocReg(CreateView): 
    model=Beneficiario
    form_class = formFichaReg
    template_name = 'plantillas/adminFicha.html' 
    success_url = reverse_lazy('HistClinica')



def calculate_age(born):
    today = date.today()
    edad= today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return edad


def exito(request):
    return render(request, 'plantillas/success.html')

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


class histClinica(CreateView):
    model = Historiaclinica
    form_class = formHistClinica
    template_name = 'plantillas/adminFicha2.html' 
    success_url = reverse_lazy('exito')








   
  

            




