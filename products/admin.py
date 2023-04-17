from django.contrib import admin

from products.models import Product
from products.models import Address


class AddressAdminInline(admin.TabularInline):
    model = Address


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description", "color", "created_at")
    fields = ("title", "image", "price", "description", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "country", "city", "address", "created_at")
    fields = ("user", "country", "city", "address", "created_at")
    readonly_fields = ("created_at",)