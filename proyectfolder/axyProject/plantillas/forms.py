from django.forms import *
from plantillas.models import Beneficiario, Historiaclinica
#from betterforms.multiform import MultiModelForm


class formFichaReg(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
           form.field.widget.attrs.update({'autocomplete': 'off'})
           self.fields['benef_id'].widget.attrs.update({'autofocus': True})
           self.fields['benef_fechanac'].widget.attrs.update({'placeholder': 'Seleccione la fecha'})
           self.fields['benef_fechanac'].widget.attrs.update({'id':'datetimepicker'})
                                  
    class Meta:
        model = Beneficiario
        fields = '__all__'
        labels = {
            'benef_id' : 'identificacion',
            'benef_nombres' : 'Nombres',
            'benef_apellidos': 'Apellidos',
            'benef_nombrepref': 'Nombre Preferido',
            'benef_sexo': 'Sexo',
            'benef_fechanac': 'Fecha de Nacimiento',
            'benef_grupoeta': 'Grupo Etareo',
            'benef_huerfano' : 'Es Huerfano',
            'benef_nav': 'Es Niño Altamente Vulnerable',
            'benef_barrio': 'Barrio',
            'benef_direccion': 'Dirección',
            'benef_telefono': 'Teléfono', 
            'benef_correo': 'Correo',
            'benef_ciudad': 'Ciudad',
            'benef_departamento': 'Departamento',
            'benef_eduformal': 'Educación Formal',
            'benef_rendiaca': 'Rendimiento Académico',
            'benef_religion' : 'Religión',
            'benef_activcrist': 'Actividades Cristianas',
            'benef_img': 'Foto',
            'benef_created' : 'Fecha de Creación',
            'benef_updated' : 'fecha de Actualización',
            'benef_hobbies' : 'Hobbies',
            'benef_materias' : 'Materias',
            'benef_deberes' : 'Deberes',

        }        
        {
            'benef_fechanac': DateField()

        }
        {
            'benef_huerfano': BooleanField(
                #attrs = {                    
                   #'placeholder':'Ingrese un nombre',                    
               # }

            )

        }
      
        {
            'benef_correo': EmailField(
                #attrs = {                    
                   #'placeholder':'Ingrese un nombre',                    
               # }

            )

        }
       

class formHistClinica(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
                                  
    class Meta:
        model = Historiaclinica
        fields = '__all__'
        labels = {
            'histclinica_beneid' : 'Beneficiario',
            'histclinica_peso': 'Peso',
            'histclinica_talla': 'Talla',
            'histclinica_tratmedico': 'Tratamiento médico',
            'histclinica_disfisica': 'Discapacidad Física',
            'histclinica_dismental': 'Discapacidad Mental',
            'histclinica_enfcronica' : 'Enfermedad crónica',
            
        }        
        






