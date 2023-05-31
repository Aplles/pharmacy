from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views import View
from models_app.models import Cart
from models_app.models import CartItem


class CartItemCreateView(View):

    def post(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=request.user)
        except ObjectDoesNotExist:
            cart = Cart.objects.create(
                user=request.user
            )
        CartItem.objects.create(
            product=kwargs["id"],
            cart=cart,
            quantity=request.POST.get("quantity", 1)
        )
        return redirect("index")
