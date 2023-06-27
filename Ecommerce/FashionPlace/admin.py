from django.contrib import admin
from .models import *

# Register your models here.
class  PaymentAdmin(admin.ModelAdmin):
    list_display  = ["id", "reference", 'amount', "verified", "date_created"]

admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductSearch)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
admin.site.register(Payment, PaymentAdmin)