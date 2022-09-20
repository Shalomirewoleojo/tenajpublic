from django.contrib import admin
from .models import *

# Register your models here.

class HomeAdmin (admin.ModelAdmin):
    list_display = ['pk', 'first_img', 'pencil_drawing', 'picture_framing',
                    'gift_box', 'greeting_card', 'training', 'appears',
                    'review1', 'review2', 'review3', 'review4']

class EnquiresAdmin (admin.ModelAdmin):
    list_display = ['sender', 'receiver']

class ProductsAdmin (admin.ModelAdmin):
    list_display = ['category', 'description']

class PricesAdmin (admin.ModelAdmin):
    list_display = ['category', ]

admin.site.register(Home, HomeAdmin)
admin.site.register(Training)
admin.site.register(Carousel)
admin.site.register(Enquires, EnquiresAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Prices, PricesAdmin)