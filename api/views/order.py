from django.shortcuts import render
from django.views import View

from models_app.models import Cart, CartItem, Order, CartItemOrder
import random


class OrderRenderCreateView(View):

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        return render(request, "cart.html", context={
            "cart_items": cart_items,
        })

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        number = ''  # предварительно создаем переменную psw
        for x in range(12):
            number = number + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        order = Order.objects.create(user=request.user, number=number, adress=request.POST['adress'],
                                     total_price=request.POST['total_price'])
        for item in cart_items:
            CartItemOrder.objects.create(order=order, cart_item=item)
        return render(request, "cart.html", context={
            "cart_items": cart_items,
        })


class OrderListView(View):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        order_items_list = []
        for order in orders:
            order_items_list.append(CartItemOrder.objects.filter(order=order))
        return render(request, "user/index.html", context={
            "orders": orders,
            "items": order_items_list
        })


class ReceptRenderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "user/recept.html")


class ReceptRender1View(View):

    def get(self, request, *args, **kwargs):
        return render(request, "user/recept2.html")
