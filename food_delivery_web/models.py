from django.db import models
from API.models import Food
from API.models import CustomUser


#//////////////////////////////////////////////// - FOR DJANGO WEBSITE - //////////////////////////////////////////////////////////////////////////#


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Food, on_delete=models.PROTECT)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.price


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_ID = models.CharField(max_length=30)
    address = models.CharField(max_length=191, blank=True)
    paid = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, default='pending')
    order_amount = models.DecimalField(max_digits=7, decimal_places=2, default=500.0)
    payment_method = models.CharField(max_length=20, blank=True)
    transaction_reference = models.CharField(max_length=20, blank=True)
    order_status = models.CharField(max_length=20, default='pending')
    # confirmed = models.DateTimeField(blank=True)
    # accepted = models.DateTimeField(blank=True)
    scheduled = models.IntegerField(default=0)
    # processing = models.DateTimeField(blank=True)
    # handover = models.DateTimeField(blank=True)
    # failed = models.DateTimeField(blank=True)
    # scheduled_at = models.DateTimeField(blank=True)
    order_note = models.CharField(max_length=350)
    delivery_charge = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    delivery_address = models.CharField(max_length=220, blank=True)
    otp = models.CharField(max_length=20, blank=True)
    # pending = models.DateTimeField(blank=True)
    # picked_up = models.DateTimeField(blank=True)
    # delivered = models.DateTimeField(blank=True)
    # canceled = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return "{} : {}".format(self.id, self.user.email)

    def total_cost(self):
        return sum([ li.cost() for li in self.lineitem_set.all() ] )


class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.product.name, self.id)

    def cost(self):
        return self.price * self.quantity
