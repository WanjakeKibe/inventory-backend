from django.contrib import admin

# Register your models here.
from .models import Category, Supplier, Product

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
