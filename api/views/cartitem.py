from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views import View
from models_app.models import Cart, Product
from models_app.models import CartItem


class CartItemCreateView(View):

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs["id"])
        cartitem = CartItem.objects.filter(product=product, cart=Cart.objects.get(user=request.user))
        if not cartitem.exists():
            if product.quantity > 0:
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

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(product_id=kwargs["id"], cart=cart)
        cart_item.delete()
        cart_items = CartItem.objects.filter(cart=cart)
        total_sum = 0
        for item in cart_items:
            total_sum += item.product.price * item.quantity
        return render(request, "basket.html", context={
            "cart_items": cart_items,
            "summ": total_sum,
        })
