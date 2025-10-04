from django.urls import path
from . import views

app_name = "compra"

urlpatterns = [
    path('fornecedor/listar', views.fornecedor_listar, name="fornecedor_listar"),
    path('fornecedor/listar/', views.fornecedor_listar, name="fornecedor_listar"),
    path('fornecedor/cadastrar', views.fornecedor_cadastrar),
    path('fornecedor/cadastrar/', views.fornecedor_cadastrar),
    path('fornecedor/remover/<int:pk>', views.fornecedor_remover),
    path('fornecedor/remover/<int:pk>/', views.fornecedor_remover)
]
