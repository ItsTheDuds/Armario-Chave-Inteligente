from django.shortcuts import render
from django.http import JsonResponse
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