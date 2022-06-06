from django.urls import path
from API.views import Home, PopularFoodListView, RecommendedFoodListView, FoodListView, FoodTypeListView


urlpatterns = [
    path('', Home, name='home'),
    path('api/foods/popular_foods/', PopularFoodListView.as_view(), name='popular_foods'),
    path('api/foods/recommended_foods/', RecommendedFoodListView.as_view(), name='recommended_foods'),
    path('api/testing', FoodListView.as_view(), name='test'),
    path('api/testing2', FoodTypeListView.as_view(), name='test2'),
]
