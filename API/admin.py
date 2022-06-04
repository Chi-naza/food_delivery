from django.contrib import admin
from API.models import CustomUser, Food_Type, Food, Product



admin.site.register(CustomUser)
admin.site.register(Food_Type)
admin.site.register(Food)
admin.site.register(Product)

