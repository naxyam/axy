from django.shortcuts import render


def plantillas(request):
    return render(request, "plantillas/adminPlantillas.html")

def fichaSocReg(request):
    return render(request, "plantillas/adminFicha.html")

def guardarInfo(request):
    benef_id=request.POST['']

def calcularEdad(request):


def getGrupeta(request):
    

def fichaSocReg2(request):
    return render(request, "plantillas/adminFicha2.html")


