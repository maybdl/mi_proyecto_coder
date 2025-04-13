from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.crear_producto, name='crear_producto'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('cliente/', views.crear_cliente, name='crear_cliente'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),

]
