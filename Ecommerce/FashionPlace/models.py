from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.lookups import IntegerFieldFloatRounding


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Categories', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True, blank=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name =  models.CharField(max_length=100)
    price = models.FloatField(default=10.55)
    image = models.ImageField()
    product_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    category = models.ManyToManyField(Category, related_name='products')
    new_arrivals = models.BooleanField(default=False)
    top_rated= models.BooleanField(default=False)
    trending = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductSearch(models.Model):
    product_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        cartitems= self.cartitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_cart_item(self):
        cartitems = self.cartitem_set.all()
        total = sum(item.quantity for item in cartitems)
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        if total == 0.00:
            self.delete()
        return total

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.address

