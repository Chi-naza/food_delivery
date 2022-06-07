from django.shortcuts import render
from API.models import Food, Products, Food_Type
from API.serializers import FoodSerializer, ProductSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.

def Home(request):
    return render(request, 'API/home.html', {"foods" : Food.objects.all()})
    
    
# For Products Model   

class PopularProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(products__food_type__type = 'P')
    
    
class RecommendedProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(products__food_type__type= 'R')
  
  
  
    
# For Food Model 
   
class PopularFoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    
    def get_queryset(self):
        return Food.objects.filter(food_type__type = 'P')
    
    
class RecommendedFoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    
    def get_queryset(self):
        return Food.objects.filter(food_type__type = 'R')
    
    