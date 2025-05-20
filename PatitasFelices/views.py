
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto
from .forms import RegistroUsuarioForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

#def login_view(request):
 #   if request.method == 'POST':
 #       username = request.POST['username']
     #  password = request.POST['password']
      #  user = authenticate(request, username=username, password=password)
       # if user:
        #    login(request, user)
         #   return redirect('home')
        #else:
         #   return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    #return render(request, 'login.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def servicios(request):
    return render(request, 'servicios.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def tienda_view(request):
    return render(request, 'tienda.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda.html', {'productos': productos})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, '¡Usuario registrado exitosamente!')
        return redirect('login')  # ✅ Redirige al login

    return render(request, 'registro.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})


def tienda(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'tienda.html', {'productos': productos})

from .forms import FormTurnos

def solicitar_turno(request):
    mensaje_enviado = False

    if request.method == 'POST':
        formulario = FormTurnos(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje_enviado = True
            formulario = FormTurnos()  # Limpia los campos luego del envío
    else:
        formulario = FormTurnos()
    
    return render(request, 'solicitar_turno.html', {
        'formulario': formulario,
        'mensaje_enviado': mensaje_enviado
    })

