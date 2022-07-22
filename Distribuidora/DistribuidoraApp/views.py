from django.shortcuts import redirect,render
from .forms import *
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def inicio(request):

        return render(request,"DistribuidoraApp/index.html",{})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"DistribuidoraApp/login.html",{"form":form})

def register_request(request):

    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"DistribuidoraApp/register.html",{"form":form})

    # form = UserCreationForm()
    form = UserRegisterForm()

    return render(request,"DistribuidoraApp/register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")