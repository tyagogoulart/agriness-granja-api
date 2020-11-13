from rest_framework import serializers
from ..models import EmailUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailUser
        fields = ['id', 'email', 'nome']