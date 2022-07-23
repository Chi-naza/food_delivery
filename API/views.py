from django.shortcuts import render, get_object_or_404
from API.models import Food, Address, CustomUser
from API.serializers import FoodSerializer, AddressSerializer, OrderSerializer, OrderDetailsSerializer
from rest_framework import generics
from rest_framework.views import APIView
# Google api view
import requests
import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
# Order
from food_delivery_web.models import Order, LineItem
from food_delivery_web import cart





TRIALS = 3 # No. of times the api call will be tried. For google map api

KEY = os.getenv('GOOGLE_API_KEY')
#print(KEY) // for testing




# For Home View or Page.

def Home(request):
    return render(request, 'API/home.html', {"foods" : Food.objects.all()})
    
      
  
  
    
# For Food Model. API getting list of food items
   
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
    
    
    

# For User Address Data. API creating or updating user address
class CreateAndUpdateAddress(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        gotten_user_id =request.data.get("user")
        myuser = CustomUser.objects.get(id = gotten_user_id)
        
        address, created = Address.objects.update_or_create(user=myuser)

        # require context={'request': request} because i'm using HyperlinkModelSerializer
        serializer = AddressSerializer(address, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

        if created:
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status.HTTP_200_OK)
        
        
    
# API view that gets specific user address.   

class UserAddressData(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=kwargs['user_id'])
        address_serializer = AddressSerializer(user.address)
        return Response(address_serializer.data)




# API for for 'SEARCH_ADDRESS_URI': google places api autocomplete 
@api_view(('GET',))
def google_places_api(request, text):
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < TRIALS:
            response = requests.get(f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={text}&key={KEY}", timeout=10)
           
            if response.status_code == 200:
                data = response.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                time.sleep(5)  # Wait for 5 seconds before re-trying
        return Response({"error": "Request failed"}, status=response.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
# API for for 'PLACES_DETAILS_URI': 
# this will get more info about a place picked by the user as we send over the placeID of that picked location to the Google API
@api_view(('GET',))
def google_place_details_api(request, place_id):
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < TRIALS:
            response = requests.get(f"https://maps.googleapis.com/maps/api/place/details/json?placeid={place_id}&key={KEY}", timeout=10)
           
            if response.status_code == 200:
                data = response.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                time.sleep(5)  # Wait for 5 seconds before re-trying
        return Response({"error": "Request failed"}, status=response.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    

# API for making a POST request. Ordering food
class MakeAnOrder(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    def create(self, request, *args, **kwargs):
        user_id = CustomUser.objects.get(id=request.data.get('user'))
        # cart_list = request.objects.get('cart')
        
        order = Order.objects.create(
            user = user_id,
            order_ID  = cart.generate_order_id(),
            order_note = request.data.get('order_note'),
            address = request.data.get('address'),
            order_amount = request.data.get('order_amount')
        )
        
        print(f'USER ID - {order.user}')
        print(f'ORDER ID - {order.order_ID}')
        
        
        # for cart_item in cart_list:
        #     li = LineItem(
        #         user = order.user,
        #         name = cart_item.product.name,
        #         ordersID = order.order_ID,
        #         product_id = cart_item.product_id,
        #         price = cart_item.price,
        #         quantity = cart_item.quantity,
        #         order_id = order.id
        #     )

        #     li.save()
        
        message = 'order made successfully'
        
        
        serializer = OrderSerializer(order, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
        
        if order: #and li:
            return Response({'order_ID': order.order_ID, 'message':message}, status.HTTP_201_CREATED)
        else:
            return Response({'error':'Order failed'}, status.HTTP_400_BAD_REQUEST)
        
        
        
        
# API for getting specific orders of a particular user
class UserOrderDetails(generics.ListAPIView):
    serializer_class = OrderDetailsSerializer
    
    def get_queryset(self):
        user_id = get_object_or_404(CustomUser, pk= self.kwargs['user_id']) 
             
        return LineItem.objects.filter(user = user_id)



    
    
    
    


