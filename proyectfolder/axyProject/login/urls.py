from django.urls import path
from login.views import LoginFormView, resetPassword

urlpatterns = [

    path('', LoginFormView.as_view(), name='Login'),
    path('olvidocontrasena.html', resetPassword, name='resetPassword'),

]
