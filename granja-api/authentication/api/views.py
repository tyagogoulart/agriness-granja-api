from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer
from ..models import EmailUser

class UserView(ModelViewSet):
    """
        retrieve: Retorna o objeto de um usuário.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = EmailUser.objects.all()
    http_method_names = ['get']

    @action(detail=False, methods=['get'])
    def perfil(self, request):
        """
            Retorna a lista de animais de uma granja. 
        """
        user = self.request.user
        queryset = EmailUser.objects.get(id=user.id)
        serializer_class = UserSerializer(queryset)
            
        return Response(serializer_class.data)
