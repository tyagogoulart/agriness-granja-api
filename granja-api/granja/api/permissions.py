from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission
from ..models import Granja

class IsResponsavelPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user:
            if obj.granja:
                return obj.granja.responsavel == request.user
            return obj.responsavel == request.user

        return False