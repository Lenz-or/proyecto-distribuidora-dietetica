from django.urls import path

from .views import *

urlpatterns = [
    # URLS de la App
    path('', inicio, name="inicio"),

]