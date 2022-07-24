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
    path('editproducto/<id>/', editarProducto, name='editproducto'),
    path('deleteProducto/<id>/', deleteProducto, name='deleteProducto'),
    path('detalleproducto/<id>/', detalleProducto, name='detalleProducto'),


    path('login/', login_request, name="login"),
    path('register', register_request, name="register"),
    path('editar_perfil', editar_perfil, name="editar_perfil"),
    path('logout', logout_request, name="logout"),

    path('viewcart/', viewcart, name="viewcart"),
    path('addcart/<producto_id>/', agregar_producto, name="addcart"),

]