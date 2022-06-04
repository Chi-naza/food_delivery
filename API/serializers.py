from dataclasses import field
from rest_framework import serializers
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from API.models import CustomUser, Food, Product


# customUser serializer overidding the one dj-rest-auth
class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=30)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone_number = self.data.get('phone_number')
        user.save()
        return user


# custom userDetails serializer to retrieve user details & info
class CustomUserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'email',
            'phone_number',
            'username',
        )
        read_only_fields = ('pk', 'email', 'phone_number', 'username',)


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['pk', 'name', 'description', 'price', 'stars', 'img', 'location', 'created_at', 'updated_at', 'food_type']
        # depth = 1  (this ppty is to enable json to nest down to a lower depth incase of foreign keys)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['total_size', 'products']
        depth = 1