from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain
from .models import Categoria, Entrada

def vista_categoria(request, nombre_categoria):
    categoria = Categoria.objects.get(nombre = nombre_categoria.capitalize())
    entradas_categoria = Entrada.objects.all().filter(categoria = categoria.id, publicado = True)

    ctx = {
        'categoria' : nombre_categoria,
        'entradas' : entradas_categoria
    }

    return render(request, 'categorias.html', ctx)

def vista_entrada(request, categoria, urlentrada):
    entrada = Entrada.objects.get(id = urlentrada)
    ctx = {
        'nombre' : entrada.nombre,
        'descripcion' : entrada.descripcion,
        'enlace' : entrada.enlace,
        'version' : entrada.version,
        'nombre_archivo' : entrada.nombre_archivo,
        'fecha' : entrada.fecha,
    }

    return render(request, 'entrada.html', ctx)