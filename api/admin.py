from django.contrib import admin
from .models import Product, Expense, Consumption, DiscardedItem

admin.site.register(Product)
admin.site.register(Expense)
admin.site.register(Consumption)
admin.site.register(DiscardedItem)
