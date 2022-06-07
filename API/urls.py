from django.urls import path
from API.views import Home, PopularFoodListView, RecommendedFoodListView, PopularProductListView, RecommendedProductListView


urlpatterns = [
    path('', Home, name='home'),
    path('api/foods/popular_foods/', PopularFoodListView.as_view(), name='popular_foods'),
    path('api/foods/recommended_foods/', RecommendedFoodListView.as_view(), name='recommended_foods'),
    path('api/products/popular/', PopularProductListView.as_view()),
    path('api/products/recommended/', RecommendedProductListView.as_view()),
]
