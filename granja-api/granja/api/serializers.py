from rest_framework import serializers

from ..models import Animal, FaseProducao, TipoGranja, Granja

class FaseProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaseProducao
        fields = ['id', 'descricao', 'sigla']

class TipoGranjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGranja
        fields = ['id', 'descricao', 'sigla']

class GranjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Granja
        fields = ['id', 'nome', 'responsavel']

class AnimalSerializer(serializers.ModelSerializer):
    fase_producao = FaseProducaoSerializer(read_only=True)
    tipo_granja = TipoGranjaSerializer(read_only=True)
    localizacao = serializers.StringRelatedField()
    raca = serializers.StringRelatedField()
    granja = serializers.StringRelatedField()
    
    class Meta:
        model = Animal
        fields = '__all__'
