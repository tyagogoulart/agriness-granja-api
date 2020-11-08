from django.utils.decorators import method_decorator
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AnimalSerializer, GranjaSerializer
from ..models import Animal, Granja
from .permissions import IsResponsavelPermission

class GranjaView(ModelViewSet):
    """
        list: Retorna a lista de granjas.
        retrieve: Retorna o objeto de uma granja específica.
        update: Atualiza uma granja específica.
        destroy: Deleta uma granja específica.
    """
    serializer_class = GranjaSerializer
    http_method_names = ['get', 'put', 'delete']
    filterset_fields = ('nome')

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'destroy':
            permission_classes = [IsResponsavelPermission]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        return Granja.objects.filter(usuarios=user.id)
    
    @action(detail=True, methods=['get'])
    def animais(self, request, pk=None):
        """
            Retorna a lista de animais de uma granja. 
        """
        user = self.request.user
        queryset = Animal.objects.filter(granja__usuarios=user, granja__id=pk)
        self.filterset_fields = ('nome', 'localizacao')
        qs = self.filter_queryset(queryset)
        page = self.paginate_queryset(qs)

        if page is not None:
            serializer_class = AnimalSerializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)
        else:
            serializer_class = AnimalSerializer(qs, many=True)
            
        return Response(serializer_class.data)

class AnimalView(ModelViewSet):
    """
        list: Retorna a lista de animais.
        retrieve: Retorna o objeto de uma granja específica.
        update: Atualiza uma granja específica.
        destroy: Deleta uma granja específica.
    """
    serializer_class = AnimalSerializer
    http_method_names = ['get', 'put', 'delete']

    def get_queryset(self):
        user = self.request.user
        print (self.request.query_params)
        return Animal.objects.filter(granja__usuarios=user)

    def get_permissions(self):
            permission_classes = [IsAuthenticated]
            if self.action == 'destroy':
                permission_classes = [IsResponsavelPermission]

            return [permission() for permission in permission_classes]
