from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductSearch)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)