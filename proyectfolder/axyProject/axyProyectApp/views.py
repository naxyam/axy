from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "axyProyectApp/index.html")

def quienesomos(request):  
    return render(request, "axyProyectApp/quienesomos.html")



