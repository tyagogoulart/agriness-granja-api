from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Granja, Animal, Localizacao, FaseProducao, TipoGranja, Raca
from .serializers import GranjaSerializer, AnimalSerializer
from authentication.models import EmailUser
from .utils import get_tokens_for_user, get_token_bearer

import json

class GranjaTests(APITestCase):
  """
  Classe de testes da API de granjas.
  """
  def setUp(self):
    self.user_responsavel = EmailUser.objects.create_user(email="responsavel@email.com", nome="Usuário Responsável")
    self.user_normal = EmailUser.objects.create_user(email="normal@email.com", nome="Usuário Normal")

  def create_granja_object(self, responsavel=None):
    if responsavel == None:
      responsavel = self.user_responsavel

    granja = Granja.objects.create(nome='Granja de teste', endereco="Av. da Paz, 431 - João Pessoa, PB", responsavel=responsavel)
    granja.usuarios.add(self.user_responsavel)
    granja.usuarios.add(self.user_normal)
    
    return granja
    
  def test_list_granjas(self):
    self.create_granja_object()
    url = reverse('granja-list')
    response = self.client.get(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    granjas = Granja.objects.filter(usuarios=self.user_responsavel.id)
    serializer = GranjaSerializer(granjas, many=True)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response['Content-Type'], 'application/json')
    self.assertEqual(response.data['results'], serializer.data)
  
  def test_create_granja(self):
    url = reverse('granja-list')
    data = { 'nome': 'Granja de teste', 'endereco': 'Av. da Paz, 431 - João Pessoa, PB', 'responsavel': self.user_responsavel.id }
    response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response['Content-Type'], 'application/json')
    self.assertEqual(Granja.objects.count(), 1)
    self.assertEqual(Granja.objects.get().nome, 'Granja de teste')

  def test_create_granja_without_credentials(self):
    url = reverse('granja-list')
    data = { 'nome': 'Granja de teste', 'responsavel': self.user_responsavel.id }
    response = self.client.post(url, data, format='json')
    msg = 'As credenciais de autenticação não foram fornecidas.'
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    self.assertEqual(response.data['detail'], msg)

  def test_create_granja_missing_required_field(self):
    url = reverse('granja-list')
    data = { 'nome': 'Granja de teste' }
    response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data['responsavel'][0], 'Este campo é obrigatório.')
    self.assertEqual(response.data['endereco'][0], 'Este campo é obrigatório.')

  def test_retrieve_granja(self):
    granja = self.create_granja_object()
    url = reverse('granja-detail', kwargs={ 'pk': granja.id })
    response = self.client.get(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    serializer = GranjaSerializer(granja)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response['Content-Type'], 'application/json')

  def test_delete_granja_as_responsavel(self):
    granja = self.create_granja_object()
    url = reverse('granja-detail', kwargs={ 'pk': granja.id })
    response = self.client.delete(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

  def test_delete_granja_as_normal_user(self):
    granja = self.create_granja_object()
    url = reverse('granja-detail', kwargs={ 'pk': granja.id })
    response = self.client.delete(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_normal))
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class AnimalTests(APITestCase):
  """
  Classe de testes da API de granjas.
  """
  def setUp(self):
    self.user_responsavel = EmailUser.objects.create_user(email="responsavel@email.com", nome="Usuário Responsável")
    self.user_normal = EmailUser.objects.create_user(email="normal@email.com", nome="Usuário Normal")
    self.granja = Granja.objects.create(nome="Granja de teste", responsavel=self.user_responsavel)
    self.granja.usuarios.add(self.user_responsavel)
    self.granja.usuarios.add(self.user_normal)
    self.fase_producao = FaseProducao.objects.create(
      descricao='teste de descrição de fase de produção',
      sigla='FASE',
    )
    self.tipo_granja = TipoGranja.objects.create(
      descricao='teste de descrição de tipo granja',
      sigla='TIPO',
    )
    self.raca = Raca.objects.create(nome="ac-7077/m")
    self.localizacao = Localizacao.objects.create(granja=self.granja, nome="Sala 5")

  def create_animal_object(self, responsavel=None):
    animal = Animal.objects.create(
        nome="SAX648",
        tipo_animal="POULTRY",
        status_animal=3,
        localizacao=self.localizacao,
        data_nascimento="2017-06-29 02:53",
        entrada_plantel="2019-06-16",
        peso_compra=98.934,
        raca=self.raca,
        codigo_rastreamento="742B7DC9863349D2A88A9AE6AC3DDABD",
        fase_producao=self.fase_producao,
        tipo_granja=self.tipo_granja,
        granja=self.granja
    )
    animal.save()
    
    return animal

  def test_list_animais(self):
    animal = self.create_animal_object()
    url = reverse('granja-animais', kwargs={ 'pk': self.granja.id })
    response = self.client.get(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    animais = Animal.objects.filter(granja__id=self.granja.id)
    serializer = AnimalSerializer(animais, many=True)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response['Content-Type'], 'application/json')
    self.assertEqual(response.data['results'], serializer.data)
  
  def test_retrieve_animal(self):
    animal = self.create_animal_object()
    url = reverse('animal-detail', kwargs={ 'pk': animal.id })
    response = self.client.get(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    queryset = Animal.objects.get(pk=animal.id)
    serializer = AnimalSerializer(queryset)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response['Content-Type'], 'application/json')

  def test_delete_animal_as_responsavel(self):
    animal = self.create_animal_object()
    url = reverse('animal-detail', kwargs={ 'pk': animal.id })
    response = self.client.delete(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
  
  def test_delete_animal_as_normal_user(self):
    animal = self.create_animal_object()
    url = reverse('animal-detail', kwargs={ 'pk': animal.id })
    response = self.client.delete(url, HTTP_AUTHORIZATION=get_token_bearer(self.user_normal))
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_create_animal(self):
    data = { 'nome': 'CPI834', 'tipo_animal': 'POULTRY', 'status_animal': 3, 'data_nascimento': '2017-07-21 00:18', 
             'entrada_plantel':'2019-05-30', 'peso_compra': 125.056, 'codigo_rastreamento':'DC7FFF687B564B48850055B8C5737485',
             'fase_producao': { 'descricao': self.fase_producao.descricao, 'sigla': self.fase_producao.sigla }, 
             'tipo_granja': { 'descricao': self.tipo_granja.descricao, 'sigla': self.fase_producao.sigla }, 
             'raca': { 'nome': self.raca.nome } }
             
    url = reverse('animal-list')
    response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    self.assertEqual(response['Content-Type'], 'application/json')

  def test_update_animal(self):
    animal = self.create_animal_object()
    data = { 'nome': animal.nome, 'tipo_animal': animal.tipo_animal, 'status_animal': 2, 'data_nascimento': animal.data_nascimento, 
             'entrada_plantel': animal.entrada_plantel, 'peso_compra': 104.184, 'codigo_rastreamento': 'DC7FFF687B564B48850055B8C5737485',
             'fase_producao': { 'descricao': self.fase_producao.descricao, 'sigla': self.fase_producao.sigla }, 
             'tipo_granja': { 'descricao': self.tipo_granja.descricao, 'sigla': self.fase_producao.sigla }, 
             'raca': { 'nome': self.raca.nome } }
             
    url = reverse('animal-detail', kwargs={ 'pk': animal.id })
    response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION=get_token_bearer(self.user_responsavel))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response['Content-Type'], 'application/json')

  