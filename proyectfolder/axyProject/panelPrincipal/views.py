from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def panelPrincipal(request):
    return render(request, 'panelPrincipal/panelPrincipal.html')