from FashionPlace.models import *
from django.contrib.sessions.models import Session
import uuid

def category_links(request):
    category = Category.objects.all()
    return {'categories': category}


def cart_render(request):
    try:
        cart = Cart.objects.get(customer=request.user.customer, completed=False)
    except:
        if request.user.is_anonymous:
            try:
                cart = Cart.objects.get(session_id = request.session['nonuser'], completed=False)
            except:
                cart = Cart.objects.create(session_id = request.session['nonuser'], completed=False)
    cartitems = cart.cartitem_set.all()
    return {'cart': cart, 
        'cartitems': cartitems
    }
