from django.shortcuts import render
from API.models import Food, Products
from API.serializers import FoodSerializer, ProductSerializer
from rest_framework import generics
from rest_framework import generics


# Create your views here.


def Home(request):
    return render(request, 'API/home.html')
    


class PopularFoodListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(products__food_type__type = 'P')
    
    
class RecommendedFoodListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(products__food_type__type= 'R')