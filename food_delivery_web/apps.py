from django.apps import AppConfig


class FoodDeliveryWebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food_delivery_web'
    
    def ready(self):
        import food_delivery_web.hooks
