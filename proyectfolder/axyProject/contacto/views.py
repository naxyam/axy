from django.shortcuts import  render, redirect
from contacto.forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method == 'POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre= request.POST.get("nombre")
            email= request.POST.get("email")
            asunto= request.POST.get("asunto")
            mensaje= request.POST.get("mensaje")

            email=EmailMessage( "Correo enviado desde Axy Software {}".format(asunto),
            "El usuario con nombre {}, con la dirección {} escribe lo siguiente: \n\n {}".format(nombre, email, mensaje), "", ["natymendieta29@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    return render(request, "contacto/contacto.html",{"miformulario":formulario_contacto})