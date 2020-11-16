import sys, os, io
from decimal import Decimal
from datetime import datetime

# Edite com o path do projeto e o python 3.8 da virtualenv em sua máquina
sys.path.append('/home/goulart/Trabalhos/desafios/agriness-granja-api/granja-api')
sys.path.append('/home/goulart/Trabalhos/desafios/env/animais/lib/python3.8/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

import django
import json
import random

django.setup()

from granja.models import Animal, FaseProducao, TipoGranja, Localizacao, Raca, Granja

try:
    with open('animais.json') as json_file:
      data = json.load(json_file)
      for obj in data:

        random_granja = random.randint(1, 3)
        granja = Granja.objects.get(id=random_granja)

        fase_producao, created = FaseProducao.objects.get_or_create(
          descricao=obj['faseProducao']['descricao'],
          sigla=obj['faseProducao']['sigla'],
        )

        tipo_granja, created = TipoGranja.objects.get_or_create(
          descricao=obj['tipoGranja']['descricao'],
          sigla=obj['tipoGranja']['sigla'],
        )

        localizacao, created = Localizacao.objects.get_or_create(
          granja=granja,
          nome=obj['localizacao'],
        )

        raca, created = Raca.objects.get_or_create(
          nome=obj['raca'],
        )

        animal = Animal()
        animal.nome = obj['nome']
        animal.granja = granja
        animal.tipo_animal = obj['tipoAnimal']
        animal.status_animal = obj['statusAnimal']
        animal.localizacao = localizacao
        animal.data_nascimento = obj['dataNascimento']
        animal.entrada_plantel = obj['entradaPlantel']
        animal.peso_compra = obj['pesoCompra']
        animal.raca = raca
        animal.codigo_rastreamento = obj['codigoRastreamento']
        animal.fase_producao = fase_producao
        animal.tipo_granja = tipo_granja

        animal.save()
        
except Exception as e:
    print (e)