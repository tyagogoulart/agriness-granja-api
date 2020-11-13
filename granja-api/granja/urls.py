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

_animais_read_only = {'get': 'animais'}
_localizacoes_read_only = {'get': 'localizacoes'}

urlpatterns = [
    path('granjas/', GranjaView.as_view(_list), name='granja-list'),
    path('granjas/<int:pk>', GranjaView.as_view(_detail), name='granja-detail'),
    path('granjas/<int:pk>/animais/', GranjaView.as_view(_animais_read_only), name='granja-animais'),
    path('granjas/<int:pk>/localizacoes/', GranjaView.as_view(_localizacoes_read_only), name='granja-localizacoes'),
    path('animais/', AnimalView.as_view(_read_only), name='animal-list'),
    path('animais/<uuid:pk>/', AnimalView.as_view(_detail), name='animal-detail'),
]