from django.urls import path
from carro import views

app_name = 'carro'

urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_a_carro, name='agregar'),
    path('eliminar/<int:producto_id>/', views.delete_product, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
]