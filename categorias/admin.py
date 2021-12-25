from django.contrib import admin
from .models import Categoria, Entrada

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


class EntradaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'categoria']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Entrada, EntradaAdmin)