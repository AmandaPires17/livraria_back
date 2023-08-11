from livraria.models import autor
from rest_framework.serializers import ModelSerializer

class AutorSerializer(ModelSerializer):
    class Meta:
        model = autor
        fields = "__all__"