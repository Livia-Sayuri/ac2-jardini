from django.shortcuts import render

# Create your views here.
# idl/api/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Hotel

def list_hotels(request):
    # Obtenha os par�metros de consulta da URL
    categoria = request.GET.get('categoria')
    tipo_quarto = request.GET.get('tipo_quarto')
    centro_turistico = request.GET.get('centro_turistico')

    # Inicialize a lista de filtros vazia
    filters = {}

    # Exemplo de filtro por categoria
    if categoria:
        filters['categoria'] = categoria

    # Exemplo de filtro por tipo de quarto
    if tipo_quarto:
        filters['tipo_quarto'] = tipo_quarto

    # Exemplo de filtro por centro tur�stico
    if centro_turistico:
        filters['centro_turistico'] = centro_turistico

    # Realize a consulta no modelo Hotel com base nos filtros
    hotels = Hotel.objects.filter(**filters)

    # Crie uma lista de dicion�rios com informa��es dos hot�is filtrados
    data = [{'nome': hotel.nome, 'categoria': hotel.categoria, 'tipo_quarto': hotel.tipo_quarto, 'centro_turistico': hotel.centro_turistico} for hotel in hotels]

    # Retorna a lista de hot�is filtrada em formato JSON
    return JsonResponse(data, safe=False)
