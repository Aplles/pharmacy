from django.contrib import admin

from models_app.models import *


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_filter = ('product',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('title',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('user', 'number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('title',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('username',)
