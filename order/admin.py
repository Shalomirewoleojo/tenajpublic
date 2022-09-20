from django.contrib import admin
from .models import *

# Register your models here.
class ShopCartAdmin (admin.ModelAdmin):
    list_display=('order_code', 'user', 'product', 'quantity', 'size', 'price', 'amount', 'order_placed')
    list_filter= ['user']
    list_display_links = ['product']
    readonly_fields = ('order_code', 'user', 'product', 'quantity', 'size', 'price', 'amount', 'order_placed')
    can_delete = False

class TrainingPurchaseAdmin (admin.ModelAdmin):
    list_display = ('course',)
    readonly_fields = ('course', 'price')
    can_delete = False


admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(TrainingPurchase, TrainingPurchaseAdmin)