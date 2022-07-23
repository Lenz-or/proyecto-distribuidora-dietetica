from django.shortcuts import get_object_or_404, redirect,render
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


# Views categorias
@login_required(login_url='/login')
def listCategorias(request):
    lista_categorias = Categorias.objects.all().order_by('nombre')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(lista_categorias, 6)
        lista_categorias = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_categorias,
            'title': 'LISTADO DE CATEGORIAS',
            'paginator': paginator
            }

    return render(request,'DistribuidoraApp/categorias.html', data)


@login_required(login_url='/login')
def addCategoria(request):
    data = {
        'form': CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect("categorias")
        else:
            data["form"] = formulario
    return render(request, 'DistribuidoraApp/agregar.html', data)

@login_required(login_url='/login')
def modificarCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)

    data = {
        'form': CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect("categorias")
        else:
            data["form"] = formulario

    return render(request, 'DistribuidoraApp/modificar-categoria.html', data)

@login_required(login_url='/login')
def deleteCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)
    categoria.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect("categorias")