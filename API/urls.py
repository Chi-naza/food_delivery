from django.urls import path
from API.views import Home, PopularFoodListView, RecommendedFoodListView, google_geocode_api, CreateAndUpdateAddress, AddressListView


urlpatterns = [
    path('', Home, name='home'),
    path('api/foods/popular_foods/', PopularFoodListView.as_view(), name='popular_foods'),
    path('api/foods/recommended_foods/', RecommendedFoodListView.as_view(), name='recommended_foods'),
    path('api/geocode/<str:lat>/<str:long>/', google_geocode_api),
    path('api/create/update/user_address/', CreateAndUpdateAddress.as_view()),
    path('api/get/user_address/', AddressListView.as_view()),
]
