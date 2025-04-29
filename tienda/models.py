from django.db import models

# Create your models here.

class Categorias_Producto(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria_producto'
        verbose_name_plural = 'categorias_producto'
        
        
    def __str__(self):
        return self.name



class Productos(models.Model):
    name = models.CharField(max_length=200)
    categorias = models.ForeignKey(Categorias_Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
    
    def __str__(self):
        return f'{self.name}, {self.precio}'
        