from django.contrib.auth.views import LoginView
from django.shortcuts import render


class LoginFormView(LoginView):
    template_name = "login/axy.html"

def resetPassword(request):
    return render(request, 'login/olvidocontrasena.html')




