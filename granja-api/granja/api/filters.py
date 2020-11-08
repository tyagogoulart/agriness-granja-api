from django_filters import FilterSet
from ..models import Animal

class AnimalFilter(FilterSet):
    class Meta:
        model = Animal
        fields = ['nome', 'localizacao']