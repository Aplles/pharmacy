from django.shortcuts import render
from django.views import View
from models_app.models import Product
from models_app.models import Category


class ProductListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "", context={
            "popular_products_1": Product.objects.all()[:5],
            "popular_products_2": Product.objects.all()[-5:],
            "categories": Category.objects.all()
        })


class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "", context={
            "product": Product.objects.get(id=kwargs["id"]),
            "categories": Category.objects.all()
        })
