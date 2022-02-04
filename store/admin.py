from django.contrib import admin
from .models import Product, Collection


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'collection',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)