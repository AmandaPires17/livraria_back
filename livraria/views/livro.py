from livraria.models.livro import Livro
from rest_framework.viewsets import ModelViewSet

from livraria.serializers import LivroSerializer, LivroDetailSerializer, LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer