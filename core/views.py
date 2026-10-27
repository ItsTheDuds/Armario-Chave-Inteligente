from django.shortcuts import render
from django.http import JsonResponse
from .utils import buscar_status_nichos_banco
from django.db import connection
# Create your views here.

def index(request):
    context = {
        'titulo': 'SENAI — Armário de Chaves',
        'nome': 'Eduardo'
    }
    return render(request, 'index.html', context)

def status_api(request):
    return JsonResponse({
        'status': 'online',
        'sistema': 'Key Track IoT'
    })
    
def status_nicho_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM vw_status_nichos;")
        dados_nichos = cursor.dictfetchall(cursor)
    return JsonResponse(dados_nichos, safe=False, status=200)