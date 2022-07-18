from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from API.models import CustomUser
from .models import Order, LineItem
from API.views import Food
from .forms import CartForm, CheckoutForm
from . import cart
# Payments
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import os


    
def food_list(request):
    all_products = Food.objects.all()
    return render(request, "food_delivery_web/index.html", {'all_products': all_products,})



def show_food(request, product_id, product_slug):
    product = get_object_or_404(Food, id=product_id)

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')

    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'food_delivery_web/product_detail.html', {'product': product, 'form': form,})





def show_cart(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'food_delivery_web/cart.html', {'cart_items': cart_items, 'cart_subtotal': cart_subtotal, })





def checkout(request):
    if request.method == 'POST':
        user_id = CustomUser(id = request.user.id)
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # created = True            
            
            o = Order(
                order_ID = cart.generate_order_id(),
                user = user_id,
                delivery_address = cleaned_data.get('delivery_address'),
                order_note = cleaned_data.get('order_note'),
            )
            o.save()            
        
        
            all_items = cart.get_all_cart_items(request)
            for cart_item in all_items:
                li = LineItem(
                    product_id = cart_item.product_id,
                    price = cart_item.price,
                    quantity = cart_item.quantity,
                    order_id = o.id
                )

                li.save()

           
            cart.clear(request)

            request.session['order_ID'] = o.order_ID
            
            print(f'ORDER ID FROM CHECKOUT: {o.order_ID}')

            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect('process_payment')


    else:
        form = CheckoutForm()
        return render(request, 'food_delivery_web/checkout.html', {'form': form})
    
    
    
    
    
#///////////////////////////////////// PAYMENT WITH PAYPAL //////////////////////////////////////////////////////////#

def process_payment(request):
    order_id = request.session.get('order_ID')
    order = get_object_or_404(Order, order_ID=order_id)
    # for testing
    # print(f'TOTAL COST - {order.total_cost()}')
    # print(f'ORDER_ID FROM SESSION - {order_id}')
    # print(f'ORDER FK ID - {order.id}')
    # print(f'ORDER USER - {order.user.username}')
    # for testing

    # What you want the button to do.
    paypal_dict = {
        "business": os.getenv('PAYPAL_RECEIVER_EMAIL'),
        "amount": '%.2f' % order.total_cost().quantize(Decimal('.01')),
        "item_name": 'Order {}'.format(order.order_ID),
        "invoice": str(order.order_ID),
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('payment_done')),
        "cancel_return": request.build_absolute_uri(reverse('payment_cancelled')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, 'food_delivery_web/process_payment.html', context)




# Process Payment For Mobile
def mobile_process_payment(request, order_ID):

    order = get_object_or_404(Order, order_ID=order_ID)
    print(f'TOTAL COST - {order.total_cost()}')
    print(f'ORDER_ID FROM SESSION - {order_ID}')
    print(f'ORDER FK ID - {order.id}')
    print(f'TOTAL COST - {order.total_cost()}')

    # What you want the button to do.
    paypal_dict = {
        "business": os.getenv('PAYPAL_RECEIVER_EMAIL'),
        "amount": '%.2f' % order.total_cost().quantize(Decimal('.01')),
        "item_name": order_ID,
        "invoice": order_ID,
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('payment_done')),
        "cancel_return": request.build_absolute_uri(reverse('payment_cancelled')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, 'food_delivery_web/process_payment.html', context)



    
    
    
# Using csrf_exempt for these views cos paypal may redirect users to them via HTTP POST request  
    
@csrf_exempt
def payment_done(request):
    return render(request, 'food_delivery_web/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'food_delivery_web/payment_cancelled.html')



