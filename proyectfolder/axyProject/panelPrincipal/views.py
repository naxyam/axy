from django.shortcuts import render



def panelPrincipal(request):
    return render(request, 'panelPrincipal/panelPrincipal.html')

def nuevodocumento(request):
    return render(request, 'panelPrincipal/adminNuevoDocumento.html')