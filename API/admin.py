from django.contrib import admin
from API.models import CustomUser, Food_Type, Food, Products, Address


class FoodAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'price']



admin.site.register(CustomUser)
admin.site.register(Food_Type)
admin.site.register(Food, FoodAdmin)
admin.site.register(Products)
admin.site.register(Address)

