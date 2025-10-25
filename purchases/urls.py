from django.urls import path
from . import views

app_name = "purchases"

urlpatterns = [
    path('supplier/create/', views.supplier_create, name='supplier_create'),
    path('supplier/recover/', views.supplier_recover, name="supplier_recover"),
    path('supplier/update/<int:pk>/', views.supplier_update, name='supplier_update'),
    path('supplier/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),
    path('supplier/search/', views.supplier_search, name="supplier_search"),

    path('ingredient/create/', views.ingredient_create, name='ingredient_create'),
    path('ingredient/recover/', views.ingredient_recover, name="ingredient_recover"),
    path('ingredient/update/<int:pk>/', views.ingredient_update, name='ingredient_update'),
    path('ingredient/delete/<int:pk>/', views.ingredient_delete, name='ingredient_delete'),
    path('ingredient/search/', views.ingredient_search, name="ingredient_search"),

    path('create/', views.purchase_create, name='purchase_create'),
    path('recover/', views.purchase_recover, name="purchase_recover"),
    path('delete/<int:pk>/', views.purchase_delete, name='purchase_delete')
]
