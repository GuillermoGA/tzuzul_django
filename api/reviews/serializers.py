from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    titulo = serializers.CharField()
    comentario = serializers.CharField()
    fecha = serializers.DateField()
