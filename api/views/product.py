import sys

from django.db.models import Value
from django.shortcuts import render
from django.views import View
from models_app.models import Product, Order, CartItemOrder, Cart
from models_app.models import Category, CartItem


class ProductListView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all().annotate(added =Value(False))
        for product in products:
            product.added=True if CartItem.objects.filter(product_id=product.id) else ""
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
        return render(request, "user/products.html", context={
            "products": product_list
        })


class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "card.html", context={
            "product": Product.objects.get(id=kwargs["id"]),
            "categories": Category.objects.all(),
            "added": True if CartItem.objects.filter(product_id=kwargs["id"],
                                                     cart=Cart.objects.get(user=request.user)
                                                     ) else "",
        })


class ProductListByCategoryView(View):

    def get(self, request, *args, **kwargs):
        vacation_1 = request.GET.get("vacation_1")
        vacation_2 = request.GET.get("vacation_2")
        price_start = request.GET.get("price_start") or 0
        price_end = request.GET.get("price_end") or sys.maxsize
        if price_start or price_end:
            products = Product.objects.filter(
                price__gte=price_start,
                price__lte=price_end,
            ).annotate(added=Value(False)).order_by(request.GET.get("radio", "id"))
        else:
            products = Product.objects.all().annotate(added=Value(False)).order_by(request.GET.get("radio", "id"))
        if vacation_1:
            products = products.filter(
                vacation=Product.NOT_RECEPT
            )
        if vacation_2:
            products = products.filter(
                vacation=Product.RECEPT
            )
        context = {}
        if kwargs.get("id") != 0:
            products = products.filter(
                category_id=kwargs["id"]
            )
            context["active_category"] = kwargs.get("id")
        for product in products:
            product.added = True if CartItem.objects.filter(product_id=product.id) else ""
        return render(request, "katalaog.html", context={
                                                            "products": products,
                                                            "categories": Category.objects.all()
                                                        } | context)


class SearchProductListView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(title__icontains=request.GET.dict().get("lname", ""))
        return render(request, "katalaog.html", context={
            "categories": Category.objects.all(),
            "products": products
        })
