from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la App
    path('', inicio, name="inicio"),
    path('register', register_request, name="register"),

]