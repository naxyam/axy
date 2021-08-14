from django.shortcuts import render


def plantillas(request):
    return render(request, "plantillas/adminPlantillas.html")

def fichaSocReg(request):
    return render(request, "plantillas/adminFicha.html")
    

def fichaSocReg2(request):
    return render(request, "plantillas/adminFicha2.html")


