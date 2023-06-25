from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your views here.
def get_cart_and_items(request):
    if request.user.is_authenticated:
        client = request.user.client
        cart, created = Cart.objects.get_or_create(client=client, completed=False)
        cartitems = cart.cartitem_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}

    return cart, cartitems


def home(request):
    cart, cartitems = get_cart_and_items(request)

    new_arrivals = Product.objects.filter(new_arrivals=True)
    top_rated = Product.objects.filter(top_rated=True)
    trending = Product.objects.filter(trending=True)

    return render(request, 'home.html', {
        'new_arrivals': new_arrivals,
        'top_rated': top_rated,
        'trending': trending,
        'cart': cart
    })


def all_products(request):
    cart, cartitems = get_cart_and_items(request)

    products = Product.objects.all()

    return render(request, 'products.html', {
        'products': products,
        'cart': cart
    })


def all_category(request, slug):
    cart, cartitems = get_cart_and_items(request)

    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)

    return render(request, 'category.html', {
        'category': category,
        'products': products,
        'cart': cart
    })


def search_product(request):
    cart, cartitems = get_cart_and_items(request)

    product_name = request.POST.get('product_name')
    searched_products = Product.objects.filter(name__icontains=product_name)

    return render(request, 'search.html', {
        'searched_products': searched_products,
        'cart': cart
    })


def cart(request):
    if request.user.is_authenticated:
        client = request.user.client
        cart, created = Cart.objects.get_or_create(client=client, completed=False)
        cartitems = cart.cartitem_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_total": 0}

    return render(request, 'cart.html', {'cartitems': cartitems,
    'cart': cart})

def updatecart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    product = Product.objects.get(product_id=product_id)
    
    if request.user.is_authenticated:
        client = request.user.client
        product = Product.objects.get(product_id=product_id)
        cart, created = Cart.objects.get_or_create(client=client, completed=False)
        cartitems, created = CartItem.objects.get_or_create(product=product, cart=cart)

        if action == 'add':
            cartitems.quantity += 1
        cartitems.save()

        msg = {
            'quantity': cart.get_cart_item
        }

    return JsonResponse(msg, safe=False)

def updatequantity(request):
    data = json.loads(request.body)
    inputval = int(data['in_val'])
    product_id = data['p_id']
    if request.user.is_authenticated:
        client = request.user.client
        product = Product.objects.get(product_id= product_id)
        cart, created = Cart.objects.get_or_create(client=client, completed=False)
        cartitems, created = CartItem.objects.get_or_create(product=product, cart=cart)

        cartitems.quantity = inputval
        cartitems.save()

        msg = {
            'subtotal':cartitems.get_total,
            'grandtotal': cart.get_cart_total,
            'quantity': cart.get_cart_item
        }

    return JsonResponse(msg, safe=False)



def checkout(request):
    cart, cartitems = get_cart_and_items(request)
    return render(request, 'checkout.html', {'cart': cart, 'cartitems': cartitems})

def payment(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        client = request.user.client
        cart, created = Cart.objects.get_or_create(client=client, completed=False)
        total = float(data['cart_total'])
        
        if total == cart.get_cart_total:
            cart.completed = True
            cart.save()
        
        
        
    return JsonResponse('It is working', safe=False)