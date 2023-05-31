from django.urls import path

from api.views.category import CategoryProductListView
from api.views.product import ProductListView
from api.views.product import ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("product/<int:id>/", ProductDetailView.as_view(), name="detail"),
    path("categories/<int:id>/product/", CategoryProductListView.as_view(), name="categories"),
]

