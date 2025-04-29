from django.contrib import admin
from servicios.models import servicios

# Register your models here.

@admin.register(servicios)
class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    