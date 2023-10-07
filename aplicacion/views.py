from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *


def home(request):
    return render(request, 'aplicacion/home.html')

#                               LOGIN DEL EMPLEADO

def login_request(request):
    if request.method == 'POST':
        miForm = AuthenticationForm(request, data = request.POST)
        if miForm.is_valid():
             usuario = miForm.cleaned_data.get('username')
             password = miForm.cleaned_data.get('password')
             user = authenticate(username = usuario, password = password)
             if user is not None:
                login(request, user)
                try:
                     avatar = Avatar.objects.get(user = request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.jpg'
                finally:
                    request.session['avatar'] = avatar 
                return render(request, 'aplicacion/base.html', {'mensaje': 'Bienvenido Sr/a {usuario}'})
             else:
                 return render(request, 'aplicacion/login.html', {'form': miForm, 'mensaje': f'Los datos ingresados NO SON CORRECTOS'})
        else:
            return render(request, 'aplicacion/login.html', {'form': miForm, 'mensaje': f'Los datos ingresados NO SON CORRECTOS'})
    miForm = AuthenticationForm()
    return render(request, 'aplicacion/login.html', {'form': miForm})


#                       SELECCION DE LA FOTO DE PERFIL DEL EMPLEADO

def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username = request.user)
            avatarIni = Avatar.objects.filter(user = u)
            if len(avatarIni) > 0:
                for i in range(len(avatarIni)):
                    avatarIni[i].delete()
            avatar = Avatar(user = u, imagen = form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user = request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request, 'aplicacion/base.html')
    else:
        form = AvatarFormulario()
    return render(request, 'aplicacion/agregarAvatar.html', {'form': form})

#                               REGISTRO DE USUARIOS/EMPLEADOS

def register(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, 'aplicacion/base.html')        
    else:
        miForm = RegistroUsuariosForm()
    return render(request, 'aplicacion/registro.html', {'form': miForm})

#                               Quienes Somos

def presentacion(request):
    contexto = {'presentacion': Presentacion.objects.all(), 'titulo': 'Inmobiliaria'}
    return render(request, 'aplicacion/presentacion.html', contexto)

class PresentacionList(ListView):
    model = Presentacion

class AgregarPresentacion(LoginRequiredMixin, CreateView):
    model = Presentacion
    fields = ['pres']
    success_url = reverse_lazy('presentacion')

class EditarPresentacion(LoginRequiredMixin, UpdateView):
    model = Presentacion
    fields = ['pres']
    success_url = reverse_lazy('presentacion')

class BorrarPresentacion(LoginRequiredMixin, DeleteView):
    model = Presentacion
    success_url = reverse_lazy('presentacion')


#                                  Contacto

def contacto(request):
    contexto = {'contacto': Contacto.objects.all(), 'titulo': 'Contacto Inmobiliaria'}
    return render(request, 'aplicacion/contacto.html', contexto)

class ContactoList(ListView):
    model = Contacto

class AgregarContacto(CreateView):
    model = Contacto
    fields = ['nombre', 'apellido', 'correo', 'telefono']
    success_url = reverse_lazy('contacto')

class EditarContacto(UpdateView):
    model = Contacto
    fields = ['nombre', 'apellido', 'correo', 'telefono']
    success_url = reverse_lazy('contacto')

class BorrarContacto(DeleteView):
    model = Contacto
    success_url = reverse_lazy('contacto')


#                                   Inmuebles

def inmueble(request):
    contexto = {'inmueble': Contacto.objects.all(), 'titulo': 'Inmuebles Disponibles'}
    return render(request, 'aplicacion/inmueble.html', contexto)

class InmuebleList(ListView):
    model = Inmueble

class AgregarInmueble(CreateView):
    model = Inmueble
    fields = ['direccion', 'piso', 'depto', 'precio', 'caracteristicas', 'fotos']
    success_url = reverse_lazy('inmueble')

class EditarInmueble(UpdateView):
    model = Inmueble
    fields = ['direccion', 'piso', 'depto', 'precio', 'caracteristicas', 'fotos']
    success_url = reverse_lazy('inmueble')

class BorrarInmueble(DeleteView):
    model = Inmueble
    success_url = reverse_lazy('inmueble')