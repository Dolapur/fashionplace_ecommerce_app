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
        request.session['nonuser'] = str(uuid.uuid4())
        cart = Cart.objects.create(session_id = request.session['nonuser'], completed=False)
    return {'cart': cart}
