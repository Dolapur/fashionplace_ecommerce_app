import json
import uuid
from .models import *
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from  .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings



# Create your views here.
def home(request):
    new_arrivals = Product.objects.filter(new_arrivals=True)
    top_rated = Product.objects.filter(top_rated=True)
    trending = Product.objects.filter(trending=True)

    return render(request, 'home.html', {
        'new_arrivals': new_arrivals,
        'top_rated': top_rated,
        'trending': trending,
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
        cart_queryset = Cart.objects.filter(customer=request.user.customer, completed=False)
        if cart_queryset.exists():
            cart = cart_queryset.first()
        else:
            cart = Cart.objects.create(customer=request.user.customer, completed=False)
        cartitems, created = CartItem.objects.get_or_create(product=product, cart=cart)

        if action == 'add':
            cartitems.quantity += 1
        cartitems.save()

        msg = {
            'quantity': cart.get_cart_item
        }
    else:
        session_id = request.session.get('session_id')
        cart, created = Cart.objects.create(session_id=session_id, completed=False)
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
    product = Product.objects.get(product_id=product_id)

    if request.user.is_authenticated:
        cart_queryset = Cart.objects.filter(customer=request.user.customer, completed=False)
        if cart_queryset.exists():
            cart = cart_queryset.first()
        else:
            cart = Cart.objects.create(customer=request.user.customer, completed=False)
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


def register_page(request):
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.save()
            session_id = request.session.session_key
            name = register_form.cleaned_data.get('name')
            customer = Customer.objects.create(user=user, name=name)
            customer.session_id = session_id
            customer.save()
            messages.info(request, "Account Created Successfully!")
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, "Registration Failed")
    else:
        register_form = CreateUserForm()

    return render(request, 'register.html', {'register_form': register_form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('checkout')
        else:
            messages.info(request, "Invalid Credentials")

    return render(request, 'login.html')


@login_required(login_url='login')
def checkout(request):
    return render(request, 'checkout.html')


def payments(request, pk):
    if request.user.is_authenticated:
        cart = Cart.objects.get(id=pk)
        cart.completed = True
        cart.save()
        messages.success(request, "Payment made successfully")
        return redirect("home")


def logout_page(request):
    logout(request)
    return redirect('home')