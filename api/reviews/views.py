from datetime import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from reviews.serializers import ReviewSerializer

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
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        Review.objects.create(titulo="", comentario="", fecha=datetime.now())