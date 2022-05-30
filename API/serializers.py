from rest_framework import serializers
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from API.models import CustomUser


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