from django.forms import ModelForm
from plantillas.models import Beneficiario#, Departamento, Ciudades, Grupoetareo,Sexo, Rendimientoacademico, Educacionformal, Actividadescristianas,Hobbies, Hobbiesxbenef, Materias, Materiasxbenef, Deberes, Deberesxbenef
from betterforms.multiform import MultiModelForm

class formFichaReg(ModelForm):
    class Meta:
        model = Beneficiario#, Departamento, Ciudades, Grupoetareo,Sexo, Rendimientoacademico, Educacionformal, Actividadescristianas,Hobbies, Hobbiesxbenef, Materias, Materiasxbenef, Deberes, Deberesxbenef
        fields = '__all__'

