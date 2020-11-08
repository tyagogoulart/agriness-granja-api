# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework import routers

from .api.views import AnimalView, GranjaView

_read_only = {'get': 'list'}

_read_only_detail = {'get': 'retrieve'}

_list = {'get': 'list',
         'post': 'create'}

_detail = {'get': 'retrieve',
           'put': 'update',
           'delete': 'destroy'}

_animais_list = {'get': 'animais'}

urlpatterns = [
    path('granjas/', GranjaView.as_view(_read_only), name='granja-list'),
    path('granjas/<int:pk>', GranjaView.as_view(_detail), name='granja-detail'),
    path('granjas/<int:pk>/animais/', GranjaView.as_view(_animais_list), name='granja-animais'),
    path('animais/', AnimalView.as_view(_read_only), name='animal-list'),
    path('animais/<uuid:pk>', AnimalView.as_view(_detail), name='animal-detail'),

    # path('clientes/', ClienteView.as_view(_list), name='cliente-list'),
    # path('clientes/<int:pk>/', ClienteView.as_view(_detail), name='cliente-detail'),

    # path('setores/', SetorView.as_view(_list), name='setor-list'),
    # path('setores/<int:pk>/', SetorView.as_view(_detail), name='setor-detail'),
    
    # path('orgaos/', OrgaoView.as_view(_list), name='orgao-list'),
    # path('orgaos/<int:pk>/', OrgaoView.as_view(_detail), name='orgao-detail'),
]

# router = NestedDefaultRouter()

# projetos_router = router.register(
#     r'projetos', 
#     ProjetoView, 
#     base_name='projetos'
# )
# projetos_router.register(
#     r'participantes', 
#     ParticipanteView, 
#     basename='projeto-participantes',
#     parents_query_lookups=['projeto']
# )
# projetos_router.register(
#     r'infraestruturas', 
#     InfraestruturaView, 
#     basename='projeto-infraestruturas',
#     parents_query_lookups=['projeto']
# )

# #router.register(r'projetos', ProjetoView, base_name='projetos')
# router.register(r'perfis', PerfilView, base_name='perfis')
# router.register(r'setores', SetorView, base_name='setores')
# router.register(r'clientes', ClienteView, base_name='clientes')

# urlpatterns = router.urls
