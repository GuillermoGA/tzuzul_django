from datetime import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

# Auth imports
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from reviews.serializers import ReviewSerializer
from reviews.serializers import ReviewModelSerielizar

from .models import Review

# Create your views here.


@api_view()
def get_reviews(request):
    reviews = Review.objects.all()
    count = Review.objects.count()

    return Response({
        "reviews": reviews,
        "number": count,
        "message": "Hola"
    })


@api_view()
def get_all_reviews(request):
    reviews = Review.objects.all()
    reviews_serializer = ReviewSerializer(reviews, many=True)
    return Response(reviews_serializer.data)


class AllReviews(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewsViewSet(ModelViewSet):
    # The order is important
    # set first the serializer_class 
    # and then the queryset
    serializer_class = ReviewModelSerielizar  # ModelViewSet uses ModelSerializer
    queryset = Review.objects.all()

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     Review.objects.create(titulo="", comentario="", fecha=datetime.now())

class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))

        if not user:
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_403_FORBIDDEN)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)

def paginaPrincipal(request):
    return render(request, "inicio.html")