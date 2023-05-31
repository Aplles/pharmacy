import sys

from django.shortcuts import render
from django.views import View
from models_app.models import Product
from models_app.models import Category


class CategoryProductListView(View):

    def get(self, request, *args, **kwargs):
        vacation = request.GET.get("vacation")
        price_start = request.GET.get("price", 0)
        price_end = request.GET.get("price", sys.maxsize)
        if vacation or price_start or price_end:
            products = Product.objects.filter(
                price__gte=price_start,
                price__lte=price_end,
                vacation=vacation,
                category_id=kwargs["id"]
            ).order_by(request.GET.get("order", "id"))
        else:
            products = Product.objects.filter(
                category_id=kwargs["id"]
            )
        return render(request, "", context={
            "products": products,
            "categories": Category.objects.all()
        })
