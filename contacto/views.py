from django.shortcuts import render, redirect
from contacto.forms import Formulario_Contacto
from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):
    if request.method == 'POST':
        formulario = Formulario_Contacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST['name']
            email = request.POST['email']
            contenido = request.POST['contenido']
            
            email= EmailMessage(subject=f'mensaje desde appDjango, el usuario con nombre {nombre}',
                                from_email=email,
                                body=contenido,
                                reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?no_valido')
            
         
    formulario = Formulario_Contacto()
    return render(request, 'contacto/contacto.html', {'formulario':formulario})