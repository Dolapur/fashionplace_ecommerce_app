from .models import *

def category_links(request):
    category = Category.objects.all()
    return {'categories': category}

def cart_renderer(request):
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(client=request.user.client, completed=False)
            cartitems = cart.cartitem_set.all()
        else:
            session_id = request.session.get('session_id')
            cart = Cart.objects.get(session_id=session_id, completed=False)
            cartitems = cart.cartitem_set.all()
    except Cart.DoesNotExist:
        cartitems = []
        cart = {"get_cart_total": 0, "get_total": 0}
        
    return {'cart': cart, 'cartitems': cartitems}