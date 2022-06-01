from django.contrib import admin
from API.models import CustomUser
from API.models import Food_Type
from API.models import Food


admin.site.register(CustomUser)
admin.site.register(Food_Type)
admin.site.register(Food)

