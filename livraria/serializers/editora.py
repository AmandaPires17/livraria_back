from livraria.models import editora
from rest_framework.serializers import ModelSerializer

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = editora
        fields = "__all__"