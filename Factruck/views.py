from django import forms
from django.contrib.auth.password_validation import password_changed
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate #libreria para autentificacion
from django.contrib import messages #libreria para enviar mensajes
from django.urls import reverse_lazy #para redireccionar a view sin url
#Librerias internas
from .Clases.method import *
from Factura.views import *

@login_required
def view_logout(request):
    logout(request)
    messages.info(request, 'Has cerrado secion')
    return redirect('login')

def view_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('factura_pdf'))
            else:
                messages.error(request, 'Usuario o contraseña equivocado')
                contexto = {'usuario' : usuario}
                return render(request, "login.html", {"form":form})
        else:
            messages.error(request, 'Usuario o contraseña equivocado')
            return render(request, "login.html", {"form":form})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form":form})