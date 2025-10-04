from django.contrib import admin
from django.urls import path, include

urlpatterns = [    
    path('', include('dashboard.urls')),
    #path('calculos/', include('calculos.urls')),
    #path('compras/', include('compras.urls')),
    #path('receitas/', include('receitas.urls')),
    path('admin/', admin.site.urls)
]