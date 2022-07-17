from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
import os
from django.shortcuts import get_object_or_404
from .models import Order

# A function which validates the payment process. When it returns successfully, paid field in Order model is set to 'True'
# It is a signal which is fired when user sends payment

def order_item_paid(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print('Payment was sucessful!!!!, pending other verifications')
        order = get_object_or_404(Order, id = ipn_obj.invoice)
        
        if (ipn_obj.mc_gross == order.total_cost() and ipn_obj.mc_currency == 'USD' and ipn_obj.receiver_email == os.getenv('PAYPAL_RECEIVER_EMAIL')):
            print('!!!. Amount, Currency and Email Verified')
            order.paid = True
            order.save()
        else:
            print('!!!! Food order item does not exist')
    else:
        print('Food order does not exist! ')



valid_ipn_received.connect(order_item_paid)