from django.contrib import admin

from models_app.models import *


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_filter = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "cart", "quantity")
    list_filter = ('product',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")
    list_filter = ('title',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "number", "cart", "adress", "total_price")
    list_filter = ('user', 'number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "category",
        "price",
        "country",
        "vacation",
        "expiration_date",
        "description",
        "quantity"
    )
    list_display_links = ("id", "title")
    list_filter = ('title',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ("Общая информация", {'fields': ['username', 'password', "email"]}),
        ('Права доступа', {'fields': ['is_superuser', 'user_permissions', 'groups', 'is_staff', 'is_active']}),
        ('Прочая информация',
         {'fields': ['last_login', 'date_joined', 'first_name', 'last_name', 'created_at', 'updated_at']}),
    ]
    list_display = (
        "id",
        "username",
        "email",
        "is_superuser",
        "created_at",
        "updated_at",
    )
    list_filter = ('username',)
