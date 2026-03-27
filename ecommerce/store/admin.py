from django.contrib import admin

from .models import Products,Customer,Orders,Category

admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Category)