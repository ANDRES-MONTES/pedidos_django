from django.urls import path
from autenticacion import views 

urlpatterns = [
    path('', views.Vregistro.as_view(), name='autenticar'),
    path('cerrar', views.cerrar, name='cerrar'),
    path('login/', views.logear, name='loguear')
]