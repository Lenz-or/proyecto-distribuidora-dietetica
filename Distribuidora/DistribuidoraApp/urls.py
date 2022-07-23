from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la App
    path('', inicio, name="inicio"),
    path('categorias/', listCategorias, name='categorias'),
    path('addcategoria/', addCategoria, name='addcategoria'),
    path('editcategoria/<id>/', modificarCategoria, name='editcategoria'),
    path('deleteCategoria/<id>/', deleteCategoria, name='deleteCategoria'),

    path('listarproductos/', listarProductos, name='listarproductos'),
        path('addproducto/', addProducto, name='addproducto'),


    path('login/', login_request, name="login"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),

]