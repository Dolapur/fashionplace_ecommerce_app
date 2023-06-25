from .models import *

def category_links(request):
    category = Category.objects.all()
    return {'categories': category}

def cart_renderer(request):
    try:
        if request.user.is_authenticated:
            client = request.user.client
            cart, created = Cart.objects.get_or_create(client=client, completed=False)
            cartitems = cart.cartitem_set.all()
        else:
            cart = Cart.objects.get(session_id=request.session['nonuser'], completed=False)
            cartitems = []
            
    except:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}
        
    return {'cart': cart, 'cartitems': cartitems}