from django.urls import path
from API.views import Home

urlpatterns = [
    path('', Home, name='home'),
]
