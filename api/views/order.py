from django.shortcuts import render
from django.views import View

from models_app.models import Cart, CartItem, Order, CartItemOrder
import random


class OrderRenderCreateView(View):

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        return render(request, "login.html", context={
            "cart_items": cart_items,
        })

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        number = ''  # предварительно создаем переменную psw
        for x in range(12):
            number = number + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        total_sum = 0
        for item in cart_items:
            total_sum += item.product.price * item.quantity
        order = Order.objects.create(user=request.user, number=number, adress=request.POST['adress'],
                                     total_price=total_sum)
        for item in cart_items:
            CartItemOrder.objects.create(order=order, product=item.product, quantity=item.quantity)
            item.delete()
        return render(request, "basket.html", context={
            "cart_items": cart_items,
        })


class OrderListView(View):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        result = []
        for order in orders:
            result += [[order, CartItemOrder.objects.filter(order=order)]]
        return render(request, "user/index.html", context={
            "result": result,
        })


class OrderItemDeleteView(View):

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(product_id=kwargs["id"], cart=cart)
        cart_item.delete()
        cart_items = CartItem.objects.filter(cart=cart)
        return render(request, "login.html", context={
            "cart_items": cart_items,
        })


class ReceptRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "user/recept.html")


class ReceptRender1View(View):

    def get(self, request, *args, **kwargs):
        return render(request, "user/recept2.html")


class UserSettingsRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "user/settings.html")
