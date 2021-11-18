from django.shortcuts import render
from rest_framework.decorators import api_view
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
    reviews_serializer = ReviewSerializer(reviews)
    return Response(reviews_serializer.data)
