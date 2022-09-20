from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('cart/', views.cart, name= 'cart'),
    path('addtoshopcart/', views.addtoshopcart, name='addtoshopcart'),
    path('updatequantity/', views.updatequantity, name='updatequantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('deletecourse/', views.deletecourse, name='deletecourse'),
    path('single_purchase/', views.single_purchase, name='single_purchase'),
    path('ordercompleted/<str:order_code>', views.ordercompleted, name='ordercompleted'),
    path('deletefromcart/<str:id>', views.deletefromcart, name='deletefromcart'),
]