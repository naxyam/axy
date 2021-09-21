from django.urls import path
from login.views import LoginFormView, resetPassword, panelPrincipal

urlpatterns = [

    path('axy.html', LoginFormView.as_view(), name='Login'),
    path('olvidocontrasena.html', resetPassword, name='resetPassword'),
    path('panelPrincipal.html', panelPrincipal, name='PanelPrincipal'),
]
