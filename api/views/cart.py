from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from models_app.models import Cart, CartItem


class CartRenderView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            total_sum = 0
            for item in cart_items:
                total_sum += item.product.price * item.quantity
            return render(request, "basket.html", context={
                "cart_items": cart_items,
                "summ": total_sum,
            })
        else:
            return render(request, "basket.html")


class CartDeleteAllView(View):

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.delete()
        return render(request, "basket.html")


class CartQuantityAddView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.get(cart=cart, product_id=kwargs["id"])
        cart_items.quantity += 1
        cart_items.save()
        cart_items = CartItem.objects.filter(cart=cart)
        total_sum = 0
        for item in cart_items:
            total_sum+=item.product.price*item.quantity

        return render(request, "basket.html", context={
            "cart_items":cart_items,
            "summ": total_sum,
        })


class CartQuantityDelView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.get(cart=cart, product_id=kwargs["id"])
        if not cart_items.quantity - 1 == 0:
            cart_items.quantity -= 1
            cart_items.save()
        cart_items = CartItem.objects.filter(cart=cart)
        total_sum = 0
        for item in cart_items:
            total_sum += item.product.price * item.quantity
        return render(request, "basket.html", context={
            "cart_items": cart_items,
            "summ": total_sum,
        })
