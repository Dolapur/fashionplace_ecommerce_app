from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from .models import *
import json
import uuid


# Create your views here.
def home(request):
    new_arrivals = Product.objects.filter(new_arrivals=True)
    top_rated = Product.objects.filter(top_rated=True)
    trending = Product.objects.filter(trending=True)

    return render(request, 'home.html', {
        'new_arrivals': new_arrivals,
        'top_rated': top_rated,
        'trending': trending
    })


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {
        'products': products
    })


def all_category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {
        'category': category,
        'products': products
    })


def search_product(request):
    product_name = request.POST.get('product_name')
    searched_products = Product.objects.filter(name__icontains=product_name)
    return render(request, 'search.html', {
        'searched_products': searched_products,
    })


def cart(request):
    return render(request, 'cart.html')

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
    else:
        session_id = request.session.get('session_id')
        product = Product.objects.get(product_id=product_id)
        cart,created = Cart.objects.get_or_create(session_id=session_id, completed=False)
        cartitems, created =CartItem.objects.get_or_create(cart=cart, product=product)
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
    
    if inputval < 0:
        # Set inputval to 0 if it's less than zero
        inputval = 0

    if request.user.is_authenticated:
        client = request.user.client
        product = Product.objects.get(product_id=product_id)
        cart, created = Cart.objects.get_or_create(client=client, completed=False)
        cartitems, created = CartItem.objects.get_or_create(product=product, cart=cart)

        cartitems.quantity = inputval
        cartitems.save()

        msg = {
            'subtotal': cartitems.get_total,
            'grandtotal': cart.get_cart_total,
            'quantity': cart.get_cart_item
        }
    else:
        session_id = request.session.get('session_id')
        product = Product.objects.get(product_id=product_id)
        cart, created = Cart.objects.get_or_create(session_id=session_id, completed=False)
        cartitems, created = CartItem.objects.get_or_create(cart=cart, product=product)

        cartitems.quantity = inputval
        cartitems.save()

        msg = {
            'subtotal': cartitems.get_total,
            'grandtotal': cart.get_cart_total,
            'quantity': cart.get_cart_item
        }

    return JsonResponse(msg, safe=False)



def checkout(request):
    return render(request, 'checkout.html')

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