from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.Serializer):
    titulo = serializers.CharField()
    comentario = serializers.CharField()
    fecha = serializers.DateField()


class ReviewModelSerielizar(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = ['__all__']  # Serialize all fields
        fields = ["id", "titulo", "comentario", "fecha", "estrellas", "movie"]  # Serialize some fields
