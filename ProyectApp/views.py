from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'ProyectApp/home.html')



def contacto(request):
    return render(request, 'ProyectApp/contacto.html')
