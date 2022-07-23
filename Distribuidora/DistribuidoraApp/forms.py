from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Productos, Categorias

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categorias
        fields = ["nombre"]

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ["nombre", "descripcion", "precio", "stock", "categoria", "oferta", "imagen"]