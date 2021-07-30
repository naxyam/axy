from django import forms

class FormularioContacto(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=200)
    email= forms.EmailField(label="Correo", max_length=200)
    asunto= forms.CharField(label="Asunto", max_length=500)
    mensaje= forms.CharField(label="Mensaje")