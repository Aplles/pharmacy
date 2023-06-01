import sys

from django.shortcuts import render
from django.views import View
from models_app.models import Product, Order, CartItemOrder
from models_app.models import Category


class ProductListView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        if len(products) > 5:
            products = products[:5]
        return render(request, "index.html", context={
            "popular_products": products,
            "categories": Category.objects.all()
        })

class ProductForCatalogListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "katalaog.html", context={
            "products": Product.objects.all(),
            "categories": Category.objects.all()
        })

class ProductForOrdersListView(View):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        product_list = []
        for order in orders:
            items = CartItemOrder.objects.filter(order=order)
            for item in items:
                product_list.append(item.cart_item.product)
        return render(request, "user_products.html", context={
            "products": product_list
        })


class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "", context={
            "product": Product.objects.get(id=kwargs["id"]),
            "categories": Category.objects.all()
        })


class ProductListByCategoryView(View):

    def get(self, request, *args, **kwargs):
        vacation = request.GET.get("vacation")
        price_start = request.GET.get("price", 0)
        price_end = request.GET.get("price", sys.maxsize)
        if vacation or price_start or price_end:
            products = Product.objects.filter(
                price__gte=price_start,
                price__lte=price_end,
                vacation=vacation or Product.NOT_RECEPT,
                category_id=kwargs["id"]
            ).order_by(request.GET.get("order", "id"))
        else:
            products = Product.objects.filter(
                category_id=kwargs["id"]
            )
        return render(request, "katalaog.html", context={
            "products": products,
            "categories": Category.objects.all()
        })
