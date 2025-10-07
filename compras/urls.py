from django.urls import path
from . import views

app_name = "compra"

urlpatterns = [
    path('fornecedor/listar/', views.fornecedor_listar, name="fornecedor_listar"),
    path('fornecedor/cadastrar/', views.fornecedor_cadastrar),    
    path('fornecedor/alterar/<int:pk>/', views.fornecedor_alterar),    
    path('fornecedor/remover/<int:pk>/', views.fornecedor_remover),

    path('insumo/listar/', views.insumo_listar, name="insumo_listar"),
    path('insumo/cadastrar/', views.insumo_cadastrar),    
    path('insumo/alterar/<int:pk>/', views.insumo_alterar),    
    path('insumo/remover/<int:pk>/', views.insumo_remover)
]
