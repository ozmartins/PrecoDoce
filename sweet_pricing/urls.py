from django.contrib import admin
from django.urls import path, include

urlpatterns = [    
    path('', include('dashboard.urls')),
    path('compra/', include('purchases.urls')),
    path('admin/', admin.site.urls)
]