from django.db import models
from django.contrib.auth.models import User
import uuid

class Granja(models.Model):
    nome = models.CharField("Nome da Granja", max_length=150)
    responsavel = models.ForeignKey(User, related_name="granja_responsavel", verbose_name="Responsável", on_delete=models.PROTECT)
    usuarios = models.ManyToManyField(User)

    def __str__(self):
        return self.nome

class Raca(models.Model):
    nome = models.CharField("Nome da Raça", max_length=150)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    granja = models.ForeignKey(Granja, verbose_name="Granja", on_delete=models.PROTECT)
    nome = models.CharField("Nome da Localização", max_length=200)

    def __str__(self):
        return self.nome

class FaseProducao(models.Model):
    descricao = models.CharField("Descrição", max_length=150)
    sigla = models.CharField("Sigla", max_length=6)

    def __str__(self):
        return self.sigla

class TipoGranja(models.Model):
    descricao = models.CharField("Descrição", max_length=150)
    sigla = models.CharField("Sigla", max_length=6)

    def __str__(self):
        return self.sigla

class Animal(models.Model):
    POULTRY = 'POULTRY'
    SWINE = 'SWINE'
    TIPO_ANIMAL_CHOICES = ((POULTRY, 'POULTRY'),
                          (SWINE, 'SWINE'),)

    class StatusAnimal(models.IntegerChoices):
        ATIVO = 0
        INATIVO = 1
        VENDIDO = 2
        DESCARTADO = 3

    id = models.UUIDField("ID do animal", primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField("Nome", max_length=100)
    granja = models.ForeignKey(Granja, verbose_name="Granja", on_delete=models.PROTECT)
    tipo_animal = models.CharField("Tipo", choices=TIPO_ANIMAL_CHOICES, default='', max_length=7)
    status_animal = models.IntegerField("Status", choices=StatusAnimal.choices, default=StatusAnimal.ATIVO)
    localizacao = models.ForeignKey(Localizacao, verbose_name="Localização na granja", on_delete=models.PROTECT)
    data_nascimento = models.DateTimeField("Data de cadastro",auto_now=False, auto_now_add=False)
    entrada_plantel = models.DateField("Data de entrada no plantel", auto_now=False, auto_now_add=False)
    peso_compra = models.DecimalField(max_digits=6, decimal_places=3)
    raca = models.ForeignKey(Raca, verbose_name="Raça", on_delete=models.PROTECT)
    codigo_rastreamento = models.CharField("Código de rastreamento", max_length=50)
    fase_producao = models.ForeignKey(FaseProducao, verbose_name="Fase de produção", on_delete=models.PROTECT)
    tipo_granja = models.ForeignKey(TipoGranja, verbose_name="Tipo de granja", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome