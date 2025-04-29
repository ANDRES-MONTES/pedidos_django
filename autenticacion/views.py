from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import Registro

# Create your views here.

class Vregistro(View):
    def get(self, request):
        form = Registro()
        return render(request, 'autenticacion/registro.html', {'form':form})
        
    
    def post(self, request):
        form = Registro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')
        else:
            for i in form.error_messages:
                messages.error(request, form.error_messages[i])
            
            return render(request, 'autenticacion/registro.html', {'form':form})

def cerrar(request):
    logout(request)
    return redirect('Home')



def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user.__dict__)
            login(request, user)
            return redirect('Home')
        else:
            for i in form.error_messages:
                messages.error(request, form.error_messages[i])
    else:
        form = AuthenticationForm()
        
        
    return render(request, 'login/login.html', {'form':form})
    
    
        
        
