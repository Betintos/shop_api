from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product


User = get_user_model()


STATUSES = {
    ("D", "Delivered"),
    ("ND", "Not Delivered")
}


PAYMENT_METHODS = {
    ("cash", "cash"),
    ("card", "card")
}


class Order(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=4, choices=STATUSES)
    payment_method = models.CharField(max_length=5, choices=PAYMENT_METHODS)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
