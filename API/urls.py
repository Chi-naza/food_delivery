from django.urls import path

from API.views import (
    Home, 
    PopularFoodListView, 
    RecommendedFoodListView, 
    google_geocode_api, 
    CreateAndUpdateAddress, 
    UserAddressData, 
    google_places_api,
    google_place_details_api,
    MakeAnOrder
)



urlpatterns = [
    path('', Home, name='home'),
    path('api/foods/popular_foods/', PopularFoodListView.as_view(), name='popular_foods'),
    path('api/foods/recommended_foods/', RecommendedFoodListView.as_view(), name='recommended_foods'),
    path('api/geocode/<str:lat>/<str:long>/', google_geocode_api),
    path('api/create/update/user_address/', CreateAndUpdateAddress.as_view()),
    path('api/get/user_address/<int:user_id>/', UserAddressData.as_view()),
    path('api/places/autocomplete/<str:text>/', google_places_api),
    path('api/place/details/<str:place_id>/', google_place_details_api),
    path('api/checkout/make_an_order/', MakeAnOrder.as_view()),
]
