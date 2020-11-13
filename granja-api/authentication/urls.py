# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework import routers

from .api.views import UserView

_read_only = {'get': 'list'}

_read_only_detail = {'get': 'retrieve'}

_perfil_read_only = {'get': 'perfil'}

urlpatterns = [
    path('usuarios/', UserView.as_view(_read_only), name='usuarios-list'),
    path('usuarios/<int:pk>/', UserView.as_view(_read_only_detail), name='usuarios-detail'),
    path('usuarios/perfil/', UserView.as_view(_perfil_read_only), name='usuarios-perfil'),
]