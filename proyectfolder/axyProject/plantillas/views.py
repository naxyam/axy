
from django.views.generic import CreateView
from plantillas.models import Beneficiario #, Departamento, Ciudades, Grupoetareo,Sexo, Rendimientoacademico, Educacionformal, Actividadescristianas,Hobbies, Hobbiesxbenef, Materias, Materiasxbenef, Deberes, Deberesxbenef
from plantillas.forms import formFichaReg


class getFicha(CreateView):
    model = Beneficiario #, Departamento, Ciudades, Grupoetareo,Sexo, Rendimientoacademico, Educacionformal, Actividadescristianas,Hobbies, Hobbiesxbenef, Materias, Materiasxbenef, Deberes, Deberesxbenef
    form_class = formFichaReg
    template_name = 'plantillas/adminFicha.html'
    success_url = 'plantillas/adminFicha2.html'
        
  

            




