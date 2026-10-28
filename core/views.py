from django.shortcuts import render
from django.http import JsonResponse
from .utils import buscar_status_nichos_banco
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
    dados_nichos = buscar_status_nichos_banco()
    return JsonResponse(dados_nichos, safe=False, status=200)
