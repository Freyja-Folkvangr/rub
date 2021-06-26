from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from UserApp.models import Cliente
from UserApp.forms import Registro, IniciarSesion


# Create your views here.
def registerView(request):
    form = Registro()
    return render(request, 'UserApp/register.html', {'form': form})

def newuser(request):
    username = request.POST['username']
    password = request.POST['password']
    telefono = request.POST['telefono']
    direccion = request.POST['direccion']
    user = User.objects.create_user(username=username, password=password)

    cliente = Cliente(user=user, telefono=telefono, direccion=direccion)
    cliente.save()

    return render(request, 'BellezaApp/index.html')

def loginView(request):
    form = IniciarSesion()
    return render(request, 'UserApp/login.html', {'form': form})
#no necesita template
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(username=username, password=password)
    login(request, usuario)
    return render(request, 'BellezaApp/index.html')
#no necesita template
def logoutView(request):
    logout(request)
    return render(request, 'BellezaApp/index.html')