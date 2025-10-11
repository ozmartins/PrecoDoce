from django.urls import path
from . import views

app_name = "purchases"

urlpatterns = [
    path('supplier/create/', views.supplier_create),
    path('supplier/recover/', views.supplier_recover, name="supplier_recover"),
    path('supplier/update/<int:pk>/', views.supplier_update),
    path('supplier/delete/<int:pk>/', views.supplier_delete),

    path('ingredient/create/', views.ingredient_create),
    path('ingredient/recover/', views.ingredient_recover, name="ingredient_recover"),
    path('ingredient/update/<int:pk>/', views.ingredient_update),
    path('ingredient/delete/<int:pk>/', views.ingredient_delete)
]
