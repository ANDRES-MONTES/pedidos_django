from django.db import models

# Create your models here.

class servicios(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        
    
    def __str__(self):
        return f'{self.titulo}'
