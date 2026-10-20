from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'titulo': 'SENAI — Armário de Chaves',
        'nome': 'Eduardo'
    }
    return render(request, 'index.html', context)