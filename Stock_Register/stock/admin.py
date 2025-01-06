from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Buy_Product)
admin.site.register(Supplier)
admin.site.register(Sell_Product)
admin.site.register(Stock)
admin.site.register(Payment)