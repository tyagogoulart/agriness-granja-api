from django_filters import rest_framework as filters
from ..models import Animal

class AnimalFilter(filters.FilterSet):
    class Meta:
        model = Animal
        fields = {
          'nome': ['exact', 'icontains'],
          'localizacao': ['exact'],
        }