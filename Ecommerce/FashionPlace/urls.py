from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.all_products, name='products'),
    path('category/<str:slug>', views.all_category, name='category'),
    path('search', views.search_product, name='product_search'),
    path('cart', views.cart, name='cart'),
    path('update_cart', views.update_cart, name="update_cart"),
    path('update_quantity', views.update_quantity, name="update_quantity"),
    path('checkout', views.checkout, name='checkout'),
	path('payment', views.payment, name="payment"),
]