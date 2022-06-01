from django.shortcuts import render
from API.models import Food
from API.serializers import FoodSerializer
from rest_framework import generics

# Create your views here.


def Home(request):
    return render(request, 'API/home.html')
    


class PopularFoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    
    def get_queryset(self):
        return Food.objects.filter(food_type__type = 'P')
    
    
class RecommendedFoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    
    def get_queryset(self):
        return Food.objects.filter(food_type__type = 'R')