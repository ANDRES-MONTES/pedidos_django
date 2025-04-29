from django.contrib import admin
from tienda import models


# Register your models here.

@admin.register(models.Categorias_Producto)
class Admin_Categorias_Producto(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    

@admin.register(models.Productos)    
class Admin_producto(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    
    

