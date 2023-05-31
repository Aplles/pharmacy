import sys

from django.shortcuts import render
from django.views import View
from models_app.models import Product
from models_app.models import Category


class CategoryProductListView(View):

    def get(self, request, *args, **kwargs):
        vacation = request.GET.get("vacation")
        if vacation:
            products = Product.objects.filter(
                price__gte=request.GET.get("price", 0),
                price__lte=request.GET.get("price", sys.maxsize),
                vacation=vacation
            ).order_by(request.GET.get("order", "id"))
        else:
            products = Product.objects.all()
        return render(request, "", context={
            "products": products,
            "categories": Category.objects.all()
        })
