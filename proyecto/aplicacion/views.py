from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from django import forms
from django.conf import settings
from .models import *
from .models import Avatar
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import MarcaForm, ClienteForm, \
                   RegistroUsuariosForm, UserEditForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
@csrf_protect
def home(request):
    return render(request, "aplicacion/home.html")


@login_required
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)
@login_required
def marcas(request):
    contexto = {'marcas': Marca.objects.all()}
    return render(request, "aplicacion/marcas.html", contexto)
@login_required
def clienteForm(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST['nombre'],
                        DNI=request.POST['DNI'],
                        email=request.POST['email']
                        )
        cliente.save()
        return HttpResponse("Se grabo con exito el cliente!")
        return render(request, "aplicacion/clienteForm.html")  
@login_required    
def clienteForm2(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get('nombre')
            cliente_DNI = miForm.cleaned_data.get('DNI')
            cliente_email = miForm.cleaned_data.get('email')
            cliente = Cliente(nombre=cliente_nombre,
                            DNI=cliente_DNI,
                            email=cliente_email)
            cliente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ClienteForm()
    
    return render(request, "aplicacion/clienteForm2.html", {"form": miForm })    
#-----------update delete cliente-------------
@login_required
def updateCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get('nombre')
            cliente.DNI = miForm.cleaned_data.get('DNI')
            cliente.email = miForm.cleaned_data.get('email')
            cliente.save()
            return redirect(reverse_lazy('clientes'))   
    else:
        miForm = ClienteForm(initial={
            'nombre': cliente.nombre,
            'DNI': cliente.DNI,
            'email': cliente.email,
        })
    return render(request, "aplicacion/clienteForm.html", {'form': miForm})
@login_required
def deleteCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))
@login_required
def createCliente(request):    
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get('nombre')
            cliente_DNI = miForm.cleaned_data.get('DNI')
            cliente_email = miForm.cleaned_data.get('email')
            cliente = Cliente(nombre=cliente_nombre, 
                            DNI=cliente_DNI,
                            email=cliente_email,
                            )
            cliente.save()
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clienteForm.html", {"form":miForm})
#-----------------15/08/2023------------------
@login_required
def updateMarca(request, id_marca):
    marca = Marca.objects.get(id=id_marca)
    if request.method == "POST":
        miForm = MarcaForm(request.POST)
        if miForm.is_valid():
            marca.marca = miForm.cleaned_data.get('marca')
            marca.modelo = miForm.cleaned_data.get('modelo')
            marca.año = miForm.cleaned_data.get('año')
            marca.save()
            return redirect(reverse_lazy('marcas'))   
    else:
        miForm = MarcaForm(initial={
            'marca': marca.marca,
            'modelo': marca.modelo,
            'año': marca.año,
        })
    return render(request, "aplicacion/marcaForm.html", {'form': miForm})
@login_required
def deleteMarca(request, id_marca):
    marca = Marca.objects.get(id=id_marca)
    marca.delete()
    return redirect(reverse_lazy('marcas'))
@login_required
def createMarca(request):    
    if request.method == "POST":
        miForm = MarcaForm(request.POST)
        if miForm.is_valid():
            marca_marca = miForm.cleaned_data.get('marca')
            marca_modelo = miForm.cleaned_data.get('modelo')
            marca_año = miForm.cleaned_data.get('año')
            marca = Marca(marca=marca_marca, 
                            modelo=marca_modelo,
                            año=marca_año,
                            )
            marca.save()
            return redirect(reverse_lazy('marcas'))
    else:
        miForm = MarcaForm()

    return render(request, "aplicacion/marcaForm.html", {"form":miForm})

#--------------Class Based View
@login_required
def patentes(request):
    contexto = {'patentes': Patente.objects.all()}
    return render(request, "aplicacion/patentes.html", contexto)

class PatenteList(LoginRequiredMixin, ListView):
    model = Patente

class PatenteCreate(LoginRequiredMixin, CreateView):
    model = Patente
    fields = ['patente', 'motor']
    success_url = reverse_lazy('patentes')

class PatenteUpdate(LoginRequiredMixin, UpdateView):
    model = Patente
    fields = ['patente', 'motor']
    success_url = reverse_lazy('patentes')

class PatenteDelete(LoginRequiredMixin, DeleteView):
    model = Patente
    success_url = reverse_lazy('patentes')

#--------------Class Based View problema averia
@login_required
def problemas(request):
    contexto = {'problemas': Problema.objects.all()}
    return render(request, "aplicacion/patentes.html", contexto)

class ProblemaList(LoginRequiredMixin, ListView):
    model = Problema

class ProblemaCreate(LoginRequiredMixin, CreateView):
    model = Problema
    fields = ['reparar', 'ingreso', 'entregado']
    success_url = reverse_lazy('problemas')

class ProblemaUpdate(LoginRequiredMixin, UpdateView):
    model = Problema
    fields = ['reparar', 'ingreso', 'entregado']
    success_url = reverse_lazy('problemas')

class ProblemaDelete(LoginRequiredMixin, DeleteView):
    model = Problema
    success_url = reverse_lazy('problemas')
    

#---------------Login / Logout / Registracion --------
#@login_required
#def login(request):
#    contexto = {'MEDIA_URL': settings.MEDIA_URL,}
#    return render(request, "aplicacion/login.html",contexto)
def login_request(request):   
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son invalidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son invalidos'})       
    miForm = AuthenticationForm()   
    return render(request, "aplicacion/login.html",{"form":miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })
