from django.urls import include, path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = 'home'),

    path('login/', login_request, name = 'login'),

    path('agregarAvatar/', agregarAvatar, name = 'agregarAvatar'),

    path('registro/', register, name = 'registro'),

    path('logout/', LogoutView.as_view(template_name = 'aplicacion/logout.html'), name = 'logout'),

    path('presentacion/', PresentacionList.as_view(), name = 'presentacion'), 
    path('AgregarPresentacion/',AgregarPresentacion.as_view(), name = 'AgregarPresentacion'),
    path('EditarPresentacion/<int:pk>/', EditarPresentacion.as_view(), name = 'EditarPresentacion'),
    path('BorrarPresentacion/<int:pk>/', BorrarPresentacion.as_view(), name = 'BorrarPresentacion'),

    path('contacto/', ContactoList.as_view(), name = 'contacto'), 
    path('AgregarContacto/',AgregarContacto.as_view(), name = 'AgregarContacto'),
    path('EditarContacto/<int:pk>/', EditarContacto.as_view(), name = 'EditarContacto'),
    path('BorrarContacto/<int:pk>/', BorrarContacto.as_view(), name = 'BorrarContacto'),

    path('inmueble/', InmuebleList.as_view(), name = 'inmueble'), 
    path('AgregarInmueble/',AgregarInmueble.as_view(), name = 'AgregarInmueble'),
    path('EditarInmueble/<int:pk>/', EditarInmueble.as_view(), name = 'EditarInmueble'),
    path('BorrarInmueble/<int:pk>/', BorrarInmueble.as_view(), name = 'BorrarInmueble'),
]