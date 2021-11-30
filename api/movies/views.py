from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieModelSerializer
from .models import Movie
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class MovieViewSet(ModelViewSet):
    serializer_class = MovieModelSerializer
    queryset = Movie.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly,]