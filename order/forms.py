from django.db.models import fields
from django.forms import ModelForm
from .models import*

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'size', 'price', 'specification']

class TrainingPurchaseForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['course','price',]

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'state']