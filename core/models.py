from django.db import models

class Unidade(models.Model):
    cod_unidade = models.AutoField(primary_key=True, verbose_name="Código da Unidade")
    ds_unidade = models.CharField(max_length=100, unique=True, verbose_name="Descrição da Unidade")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")

    def __str__(self):
        return self.ds_unidade
    
class Usuario(models.Model):
    class perfil(models.TextChoices):
        MASTER_GERAL = "MASTER_GERAL", "Usuário Master Geral"
        MASTER_UNIDADE = "MASTER_UNIDADE", "Usuário Master da Unidade"
        COORDENADOR = "COORDENADOR", "Usuário Coordenador"
        DOCENTE = "DOCENTE", "Usuário Docente"
        PORTARIA = "PORTARIA", "Usuário Portaria"
        
    cod_usuario = models.AutoField(primary_key=True, verbose_name="Código do Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome do Usuário")
    email = models.EmailField(unique=True, verbose_name="Email do Usuário", blank=True, null=True)
    uuid = models.CharField(max_length=8, unique=True, verbose_name="UUID do Usuário", blank=True, null=True)
    unidades = models.ManyToManyField(Unidade, verbose_name="Unidades do Usuário")
    perfil = models.CharField(choices=perfil.choices, verbose_name="Perfil do Usuário", default=perfil.DOCENTE)
    st_ativo = models.BooleanField(default=True, verbose_name="Status do Usuário")

    def __str__(self):
        return self.nome
    
class Espaco(models.Model):
    cod_espaco = models.AutoField(primary_key=True, verbose_name="Código do Espaço")
    ds_espaco = models.CharField(max_length=100, unique=True, verbose_name="Descrição do Espaço", blank=True, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, verbose_name="Unidade")
    st_disponivel = models.BooleanField(default=True, verbose_name="Status de Disponibilidade do Espaço")

    def __str__(self):
        return self.ds_espaco
    
class Chave(models.Model):
    cod_chave = models.AutoField(primary_key=True, verbose_name="Código da Chave")
    num_chave = models.CharField(max_length=50, unique=True, verbose_name="Número da Chave", blank=True, null=True)
    espaco = models.OneToOneField(Espaco, verbose_name="Espaço", on_delete=models.CASCADE)
    uuid_tag_chave = models.CharField(max_length=50, unique=True, verbose_name="UUID da Tag da Chave", blank=True, null=True)
    st_disponivel = models.BooleanField(default=True, verbose_name="Status de Disponibilidade da Chave")

    def __str__(self):
        return self.num_chave