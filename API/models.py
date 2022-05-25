from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]


class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION, default='Male')
    phone_number = models.CharField(max_length=20)
    
    
    
    
    




# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
# from datetime import date
# class User(AbstractUser):
#    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#    email = models.EmailField(_('email address'), unique = True)
#    native_name = models.CharField(max_length = 5)
#    phone_no = models.CharField(max_length = 10)
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#    def __str__(self):
#        return "{}".format(self.email)
