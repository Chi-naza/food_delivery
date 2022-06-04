from django.db import models
from django.contrib.auth.models import AbstractUser



GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]

FOOD_TYPE = [
    ('P', 'Popular'),
    ('R', 'Recommended'),
]


class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION, default='Male')
    phone_number = models.CharField(max_length=20)
    


class Food_Type(models.Model):
    type = models.CharField(max_length=20, choices=FOOD_TYPE)
    description =  models.CharField(max_length=220)
    
    def __str__(self):
        return self.type
    


class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    location = models.CharField(max_length=220) 
    stars = models.CharField(max_length=10)
    description = models.TextField()
    quantity = models.IntegerField()
    people = models.IntegerField()
    selected = models.IntegerField()
    img = models.ImageField(upload_to='food_image')
    food_type = models.ForeignKey(Food_Type, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    quantity_Ordered = models.IntegerField(default=0)
    products = models.ForeignKey(Food, on_delete=models.CASCADE)
      

# p = Food(name = food['name'], price = food['price'], location = food['location'], stars = food['stars'], description = food['description'], quantity = food['quantity'], people = food['people'], selected = food['selected'], img = food['img'], food_type = food['food_type'], created_at = food['created_at'], updated_at = food['updated_at'])

    




#    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#    email = models.EmailField(_('email address'), unique = True)
#    native_name = models.CharField(max_length = 5)
#    phone_no = models.CharField(max_length = 10)
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#    def __str__(self):
#        return "{}".format(self.email)

