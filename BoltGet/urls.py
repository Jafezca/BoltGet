from django.contrib import admin
from django.urls import path, include
from .views import inicio
import categorias.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('categorias/', include(categorias.urls)),
]
