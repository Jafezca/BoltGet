from django.urls import path
from .views import vista_categoria, vista_entrada

urlpatterns = [
    path('<str:nombre_categoria>/', vista_categoria, name='listacategorias'),
    path('<str:categoria>/entrada/<str:urlentrada>', vista_entrada, name='entrada'),
]