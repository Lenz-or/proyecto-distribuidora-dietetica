from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la App
    
    path('nosotros/', nosotros, name='nosotros'),
    path('categorias/', listCategorias, name='categorias'),
    path('addcategoria/', addCategoria, name='addcategoria'),
    path('editcategoria/<id>/', modificarCategoria, name='editcategoria'),
    path('deleteCategoria/<id>/', deleteCategoria, name='deleteCategoria'),

    path('listarproductos/', listarProductos, name='listarproductos'),
    path('addproducto/', addProducto, name='addproducto'),
    path('editproducto/<id>/', editarProducto, name='editproducto'),
    path('deleteProducto/<id>/', deleteProducto, name='deleteProducto'),
    path('detalleproducto/<id>/', detalleProducto, name='detalleProducto'),
    path('productocategoria/<id>/', productoxCategoria, name='productocategoria'),


    path('login/', login_request, name="login"),
    path('register', register_request, name="register"),
    path('editar_perfil', editar_perfil, name="editar_perfil"),
    path('logout', logout_request, name="logout"),

    path('viewcart/', viewcart, name="viewcart"),
    path('addcart/<producto_id>/', agregar_producto, name="addcart"),
    path('restarcart/<producto_id>/', restar_producto, name="restarcart"),
    path('delcart/<producto_id>/', eliminar_producto, name="delcart"),
    path('cleancart/', limpiar_carrito, name="cleancart"),
    


]