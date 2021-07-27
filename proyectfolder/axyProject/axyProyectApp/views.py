from django.shortcuts import render, HttpResponse
import datetime



# Create your views here.

def index(request):
    return render(request, "axyProyectApp/index.html")

def quienesomos(request):  
    return render(request, "axyProyectApp/quienesomos.html")


def contacto(request):
    return render(request, "axyProyectApp/contacto.html")

def login(request):
    return render(request, "axyProyectApp/axy.html")

