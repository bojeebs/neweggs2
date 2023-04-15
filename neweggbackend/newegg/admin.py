from django.contrib import admin
from .models import Product, ShoppingCart, OrderDetails, User


admin.site.register(User)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(OrderDetails)