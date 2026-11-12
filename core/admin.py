from django.contrib import admin
from .models import Unidade, Usuario, UsuarioUnidade, Espaco, Chave

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ("cod_unidade", "ds_unidade", "endereco")
    search_fields = ("ds_unidade", "endereco")
    
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("cod_usuario", "nome")
    search_fields = ("nome",)

@admin.register(UsuarioUnidade)
class UsuarioUnidadeAdmin(admin.ModelAdmin):
    list_display = ("cod_usuario_unidade", "usuario", "unidade")
    search_fields = ("usuario__nome", "unidade__ds_unidade")

@admin.register(Espaco)
class EspacoAdmin(admin.ModelAdmin):
    list_display = ("cod_espaco", "ds_espaco", "unidade")
    search_fields = ("ds_espaco", "unidade__ds_unidade")

@admin.register(Chave)
class ChaveAdmin(admin.ModelAdmin):
    list_display = ("cod_chave", "num_chave", "espaco")
    search_fields = ("num_chave", "espaco__ds_espaco")