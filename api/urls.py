from django.urls import path
from api.views.user import UserLoginRegisterView, logout_view, UserUpdateInfoView, UserUpdatePasswordView, UserLoginRenderView, UserRegisterRenderView
from api.views.cart import CartRenderView, CartDeleteAllView
from api.views.cartitem import CartItemCreateView, CartItemDeleteView
from api.views.product import ProductListView, ProductDetailView, ProductListByCategoryView, ProductForOrdersListView, \
    ProductForCatalogListView, SearchProductListView
from api.views.order import OrderRenderCreateView, OrderListView

urlpatterns = [
    # product
    path("", ProductListView.as_view(), name="index"),
    path("catalog/", ProductForCatalogListView.as_view(), name="catalog"),
    path("product/<int:id>/", ProductDetailView.as_view(), name="detail"),
    path("categories/<int:id>/product/", ProductListByCategoryView.as_view(), name="categories"),

    path("search/", SearchProductListView.as_view(), name="search"),

    # cart
    path("cart/", CartRenderView.as_view(), name="cart"),
    path("cart/delete_all/", CartDeleteAllView.as_view(), name="clear_cart"),

    # cart items
    path("cart/product/<int:id>/create/", CartItemCreateView.as_view(), name="add_to_cart"),
    path("cart/product/<int:id>/delete/", CartItemDeleteView.as_view(), name="delete_from_cart"),

    # order
    path("order/", OrderRenderCreateView.as_view(), name="order"),
    path("order/list/", OrderRenderCreateView.as_view(), name="order"),

    # user
    path('user/', UserLoginRegisterView.as_view(), name='user'),
    path('user/login/', UserLoginRenderView.as_view(), name='login'),
    path('user/register/', UserRegisterRenderView.as_view(), name='register'),
    path('user/', UserLoginRegisterView.as_view(), name='user'),
    path('user/logout/', logout_view, name='logout'),
    path('user/orders/', OrderListView.as_view(), name='user_orders'),
    path('user/products/', ProductForOrdersListView.as_view(), name='user_products'),
    path('user/change_info/', UserUpdateInfoView.as_view(), name='user_info'),
    path('user/change_pass/', UserUpdatePasswordView.as_view(), name='user_pass'),
]
