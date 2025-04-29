from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, Linea_Pedido
from carro.carro import Carro
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import  render_to_string
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url="/autenticacion/login/")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user_id_id=request.user.id)
    carro = Carro(request)
    lineas_pedido = []
    for i, j in carro.carro.items():
        lineas_pedido.append(Linea_Pedido(
            user_id_id=request.user.id,
            producto_id_id=i,
            pedido_id_id = pedido.id,
            cantidad = j['cantidad']
        ))
        
    Linea_Pedido.objects.bulk_create(lineas_pedido)
    enviar_email(pedido=pedido,
                 lineas_pedido=lineas_pedido,
                 usuario=request.user.username,
                 email_user = request.user.email)
    
    messages.success(request, 'el pedido se ha creado correctamente')
    carro.delete_all()
    return redirect('/tienda')
    # 
    
    
def enviar_email(**kwargs):
    asunto = 'Gracias por el pedido'
    datos = render_to_string('emails/pedido.html', {
        'pedido': kwargs.get('pedido'),
        'articulos': kwargs.get('lineas_pedido'),
        'user': kwargs.get('usuario'),    
        })
    
    mensaje = strip_tags(datos)
    from_email = 'ejemplo@gmail.com'
    to_email = kwargs.get('email_user')
    
    send_mail(asunto, mensaje, from_email, [to_email], fail_silently=False, html_message=datos)
    
