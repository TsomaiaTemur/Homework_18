from django.contrib import admin
from .models import LoyalCustomer, Product
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    list_display = ('name','type','quality','quantity','timestamp')
    search_fields = ('name','type','timestamp')
admin.site.register(LoyalCustomer)
admin.site.register(Product, CustomAdmin)
