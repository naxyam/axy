from django.shortcuts import render, redirect
from plantillas.models import Departamento, Beneficiario, Ciudades, Grupoetareo,
from django.utils import timezone
from 

def getFichaSocialRegistro(request):
    if request.method == 'POST':
        depa = Departamento.objects.all()
        bene = Beneficiario.objects.all()
        ciu = Ciudades.objects.all()
        grupeta = Grupoetareo.objects.all()
        if formulario_contacto.is_valid():
            nombre= request.POST.get("nombre")
            email= request.POST.get("email")
            asunto= request.POST.get("asunto")
            mensaje= request.POST.get("mensaje")

            

    return render(request, "contacto/contacto.html",{"miformulario":formulario_contacto})


def guardarInfo(request):
    benef_id=request.POST['']

def calcularEdad(request):


def getGrupeta(request):
    

def fichaSocReg2(request):
    return render(request, "plantillas/adminFicha2.html")


