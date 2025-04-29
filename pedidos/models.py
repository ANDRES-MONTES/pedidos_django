from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Productos
from django.db.models import F, Sum, FloatField

# Create your models here.
User = get_user_model()

class Pedido(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='Pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']
        
    def __str__(self):
        return f'{self.id} - {self.user_id}, {self.user_id.first_name}'
    
    @property
    def total(self):
        return self.linea_pedido_set.aggregate(
                total = Sum(F('producto_id__precio') * F('cantidad'), output_field=FloatField())
        )['total'] or 0
    
    
class Linea_Pedido(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.name}'
    
    class Meta:
        db_table='linea pedidos'
        verbose_name = 'linea pedido'
        verbose_name_plural = 'lineas pedidos'
        ordering = ['id']