from django.shortcuts import render
from django.views import View


class ProductListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "", context={

        })


class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "", context={

        })
