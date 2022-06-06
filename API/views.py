from django.shortcuts import render
from API.models import Food, Products, Food_Type
from API.serializers import FoodSerializer, ProductSerializer, FoodTypeSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.

def Home(request):
    return render(request, 'API/home.html', {"foods" : Food.objects.all()})
    
    
    
    
    
    

class PopularFoodListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(products__food_type__type = 'P')
    
    
class RecommendedFoodListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(products__food_type__type= 'R')
    
    
    
class FoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    
    def get_queryset(self):
        return Food.objects.all()
    
class FoodTypeListView(generics.ListAPIView):
    serializer_class = FoodTypeSerializer
    
    def get_queryset(self):
        return Food_Type.objects.all()
    
    


# class PopularFoodListView(generics.AP):
#     serializer_class = ProductSerializer
    
#     def get_queryset(self):
#         return Products.objects.filter(products__food_type__type = 'P')
    
    
# class RecommendedFoodListView(generics.ListAPIView):
#     serializer_class = ProductSerializer
    
#     def get_queryset(self):
#         return Products.objects.filter(products__food_type__type= 'R')