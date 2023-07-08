from FashionPlace.models import *
from django.contrib.sessions.models import Session
import uuid

def category_links(request):
    category = Category.objects.all()
    return {'categories': category}

def cart_render(request):
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(customer=request.user.customer, completed=False)
            cartitems = cart.cartitem_set.all()
        else:
            session_id = request.session.get('session_id')
            if session_id not in request.session:
                session_id = str(uuid.uuid4())
                request.session['session_id'] = session_id
                request.session.save()

            cart = Cart.objects.get(session_id=session_id, completed=False, customer_id=None)               
            cartitems = cart.cartitem_set.all()
    except Cart.DoesNotExist:
        cartitems = []
        cart = {"get_cart_total": 0, "get_total": 0}
        
    return {'cart': cart, 'cartitems': cartitems}