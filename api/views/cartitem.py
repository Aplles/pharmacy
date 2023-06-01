from django.shortcuts import redirect
from django.views import View
from models_app.models import Cart
from models_app.models import CartItem


class CartItemCreateView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        CartItem.objects.create(
            product=kwargs["id"],
            cart=cart,
            quantity=request.POST.get("quantity", 1)
        )
        return redirect("index")


class CartItemDeleteView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(pk=kwargs["id"])
        cart_item.delete()
        return redirect("index")
