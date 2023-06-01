from django.shortcuts import redirect, render
from django.views import View
from models_app.models import Cart, Product
from models_app.models import CartItem


class CartItemCreateView(View):

    def get(self, request, *args, **kwargs):
        if not CartItem.objects.filter(product=Product.objects.get(id=kwargs["id"]), cart=Cart.objects.get(user=request.user)).exists():
            CartItem.objects.create(
                product=Product.objects.get(id=kwargs["id"]),
                cart=Cart.objects.get(user=request.user),
                quantity=request.GET.get("quantity", 1)
            )
        return render(request, "card.html", context={
            "product": Product.objects.get(id=kwargs["id"]),
            "added": True if CartItem.objects.filter(product_id=kwargs["id"],
                                                     cart=Cart.objects.get(user=request.user)
                                                     ).exists() else "",
        })


class CartItemDeleteView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(pk=kwargs["id"])
        cart_item.delete()
        return redirect("index")
