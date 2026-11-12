from django.db import models

class Unidade(models.Model):
    cod_unidade = models.AutoField(primary_key=True, verbose_name="Código da Unidade")
    ds_unidade = models.CharField(max_length=100, unique=True, verbose_name="Descrição da Unidade")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")

    def __str__(self):
        return self.ds_unidade
    
class Usuario(models.Model):
    cod_usuario = models.AutoField(primary_key=True, verbose_name="Código do Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome do Usuário")

    def __str__(self):
        return self.nome
    
class UsuarioUnidade(models.Model):
    cod_usuario_unidade = models.AutoField(primary_key=True, verbose_name="Código do Usuário-Unidade")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, verbose_name="Unidade")

    def __str__(self):
        return f"{self.usuario.nome} - {self.unidade.ds_unidade}"
    
class Espaco(models.Model):
    cod_espaco = models.AutoField(primary_key=True, verbose_name="Código do Espaço")
    ds_espaco = models.CharField(max_length=100, unique=True, verbose_name="Descrição do Espaço")
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, verbose_name="Unidade")

    def __str__(self):
        return self.ds_espaco
    
class Chave(models.Model):
    cod_chave = models.AutoField(primary_key=True, verbose_name="Código da Chave")
    num_chave = models.CharField(max_length=50, unique=True, verbose_name="Número da Chave")
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE, verbose_name="Espaço")

    def __str__(self):
        return self.num_chave