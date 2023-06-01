from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from models_app.models import Cart, CartItem


class CartRenderView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            return render(request, "basket.html", context={
                "cart_items": cart_items,
                "summ":  CartItem.objects.aggregate(Sum('product__price')),
            })
        else:
            return render(request, "basket.html")


class CartDeleteAllView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.delete()
        return render(request, "cart.html")
