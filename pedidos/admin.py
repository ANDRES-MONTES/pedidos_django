from django.contrib import admin
from .models import Pedido, Linea_Pedido

# Register your models here.

@admin.register(Pedido)
class Pedido_Admin(admin.ModelAdmin):
    list_display = ('user_id', 'created_at')
    
@admin.register(Linea_Pedido)
class Linea_pedido_admin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    
    
    
