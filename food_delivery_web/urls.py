from django.urls import path
from food_delivery_web.views import food_list, show_food, show_cart, checkout, process_payment, mobile_process_payment, payment_done, payment_canceled

urlpatterns = [
    path('food/list/', food_list, name='index'),
    path('food/<int:product_id>/<slug:product_slug>/', show_food, name='product_detail'),
    path('food/cart/', show_cart, name='show_cart'),
    path('food/checkout/', checkout, name='checkout'),
    path('process-payment/', process_payment, name='process_payment'),
    path('process-paypal-payment/<str:order_ID>/', mobile_process_payment),
    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),
]