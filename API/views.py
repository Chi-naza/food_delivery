from django.shortcuts import render
from API.models import Food, Products
from API.serializers import FoodSerializer, ProductSerializer
from rest_framework import generics
# Google api view
import requests
import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

TRIALS = 3 # No. of times the api call will be tried. For google map api

KEY = os.getenv('GOOGLE_API_KEY')
print(KEY)




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
    
    
    
# For Google Map Api. Making a call to an external api & Rendering it through djangorestframework
@api_view(('GET',))
def google_geocode_api(request, lat, long):
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < TRIALS:
            r = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&key={KEY}", timeout=10)
            if r.status_code == 200:
                data = r.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                time.sleep(5)  # Wait for 5 seconds before re-trying
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    
