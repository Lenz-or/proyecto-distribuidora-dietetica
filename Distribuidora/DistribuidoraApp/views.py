from django.shortcuts import render

# Create your views here.


def inicio(request):

        return render(request,"DistribuidoraApp/index.html",{})