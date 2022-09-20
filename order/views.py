from django.shortcuts import render, redirect
import uuid

from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from users.models import UserProfile
import json
import requests
import random
import string
import uuid
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
@login_required(login_url='/login')
def addtoshopcart(request):
    url = request.META.get('HTTP_REFERER')
    thequantity = int(request.POST['quantity'])
    thesize = request.POST.get('size', None)
    theprodid = request.POST['prodid']
    theprice = request.POST.get('price', None)
    specification = request.POST.get('specification', None)
    aprod = Products.objects.get(pk=theprodid)

    cart = ShopCart.objects.filter(order_placed=False).filter(user__username = request.user.username)

    if cart:
        prodchecker = ShopCart.objects.filter(product_id = aprod.id, size=thesize, quantity = thequantity, user__username = request.user.username, specification=specification).first()

        if prodchecker: #product exists in the cart, increment it
            prodchecker.quantity += thequantity
            prodchecker.size = thesize
            prodchecker.save()
            messages.success(request, "Product added to Shopcart")
            return redirect(url)

        else: # product is not in the cart, add it
            if theprice is not None:
                anitem = ShopCart()
                anitem.product=aprod
                anitem.user=request.user
                anitem.order_code=cart[0].order_code
                anitem.quantity=thequantity
                anitem.specification=specification
                anitem.size=thesize
                anitem.price=theprice
                anitem.order_placed=False
                anitem.save()
                messages.success(request, "Product added to Shopcart")
            else: messages.warning(request, 'Please pick a size')


    else: #create a new cart, generate order code
        if theprice is not None:
            ordercode = str(uuid.uuid4())
            newcart = ShopCart()
            newcart.product=aprod
            newcart.user=request.user
            newcart.order_code=ordercode
            newcart.quantity=thequantity
            newcart.specification=specification
            newcart.size=thesize
            newcart.price=theprice        
            newcart.order_placed=False
            newcart.save()
            messages.success(request, "Product added to Shopcart")
        else: messages.warning(request, 'Please pick a size')


    return redirect(url)

def cart (request):
    prodchecker = ShopCart.objects.filter(user__username = request.user.username, order_placed= False)
    subtotal=0
    vat = 0
    total= 0

    for item in prodchecker:
        subtotal += item.price * item.quantity

    vat = 0.075 * subtotal
    total = subtotal + vat

    context = {
        'prodchecker': prodchecker,
        'vat': vat,
        'total': total,
    }

    return render (request, 'cart.html', context)


@require_POST
@login_required(login_url='/login')
def updatequantity(request):
    url= request.META.get('HTTP_REFERER')
    newquantity = request.POST['itemquantity']
    theitem = ShopCart.objects.get(id=request.POST['itemid'])
    theitem.quantity = newquantity
    theitem.save()

    messages.success(request, "Product Quantity successsfully updated")
    return redirect(url)

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Item deleted from Shopcart.')
    return redirect('order:cart')

@login_required(login_url='/login')
def checkout (request):
    pendraw = Products.objects.filter(category= 'Pencil Drawings')
    picframe = Products.objects.filter(category= 'Picture Framing')
    prodchecker = ShopCart.objects.filter(user__username = request.user.username, order_placed= False)
    client = User.objects.get(username=request.user.username)
    client2 = Order.objects.filter(user=request.user).first()
    subtotal=0
    vat = 0
    total= 0

    for item in prodchecker:
        if item.product.category == 'Picture Framing' or item.product.category == 'Pencil Drawings':
            subtotal += item.price * item.quantity

    vat = 0.075 * subtotal
    total = subtotal + vat

    context = {
        'prodchecker': prodchecker,
        'vat': vat,
        'total': total,
        'pendraw': pendraw,
        'client': client,
        'client2': client2,
        'picframe': picframe,
    }

    return render (request, 'check_out.html', context)

@require_POST
@login_required(login_url='/login')
def placeorder(request):
    api_key = 'sk_live_b8c0ebd1db821c213d0ac1d65752ef44a2e39448'
    url = 'https://api.paystack.co/transaction/initialize'
    ordercode =  request.POST['order_number']
    callback_url = 'http://127.0.0.1:8000/order/ordercompleted/code'
    autogen_ref = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
    current_user = User.objects.get(username = request.user.username)
    user = UserProfile.objects.get(user_id = current_user.id)
    total = float(request.POST['amount']) * 100    
    

    headers = {'Authorization': f'Bearer {api_key}'}
    data = {'reference': autogen_ref, 'amount':int(total), 'order_number':ordercode, 'email':user.email, 'callback_url':callback_url }

    
    # making a request to PAYSTACK 
    try:
        r = requests.post(url, headers=headers, json=data)
    except Exception:
        messages.error(request, 'Network busy. Please try again in few minutes. Thank You!')
    else:
        # create an order 
        transback = json.loads(r.text)
        
        rd_url = transback['data']['authorization_url']
        theuser= UserProfile.objects.filter(user=request.user).first()
        order = Order()
        order.user=theuser.user
        order.first_name=theuser.user.first_name
        order.last_name=theuser.user.last_name
        order.phone=theuser.phone
        order.city=theuser.city
        order.state=theuser.state
        order.order_code= ordercode
        order.payment_code = autogen_ref
        order.total=total
        order.order_placed = True
        order.save()

        profile= UserProfile.objects.get(user__username = request.user.username)
        shopcart= ShopCart.objects.filter(order_placed=False).filter(user__username= request.user.username)
        cart = TrainingPurchase.objects.filter(order_placed=False).filter(user__username = request.user.username)

        #cleaning the shopcart
        for item in shopcart:
            if item.product.category == 'Picture Framing' or item.product.category == 'Pencil Drawings':
                item.order_placed= True
                item.save()

        for item in cart:
            item.order_placed= True
            item.save()
        return redirect(rd_url)
    return redirect('order:checkout')

@login_required(login_url='/login')
def single_purchase(request):
    thecourse = request.POST.get('course', None)
    total = request.POST.get('price', None)
    client = User.objects.get(username=request.user.username)
    client2 = Order.objects.filter(user=request.user).first()

    cart = TrainingPurchase.objects.filter(order_placed=False).filter(user__username = request.user.username,)

    if cart:
        messages.warning(request, 'A course already in cart')

    else:
        ordercode = str(uuid.uuid4())
        anitem = TrainingPurchase()
        anitem.user=request.user
        anitem.order_code=ordercode
        anitem.course=thecourse
        anitem.price=total
        anitem.order_placed=False
        anitem.save()

    context = {
        'thecourse': thecourse,
        'total': total,
        'client': client,
        'client2': client2,
    }

    return render (request, 'training_purchase.html', context)

@login_required(login_url='/login')
def deletecourse(request):
    TrainingPurchase.objects.get(user= request.user, order_placed=False).delete()
    # messages.success(request, 'Item deleted from Shopcart.')
    return redirect('training')

@login_required(login_url='/login')
def ordercompleted(request, order_code):
    profile= UserProfile.objects.get(user__username = request.user.username)
    shopcart= ShopCart.objects.filter(order_placed=False).filter(user__username= request.user.username)
    cart = TrainingPurchase.objects.filter(order_placed=False).filter(user__username = request.user.username,)

    #cleaning the shopcart
    # for item in shopcart:
    #     item.order_placed= True
    #     item.save()

        #reducing quantity instock
        # aproduct = Product.objects.get(id=item.product.id)
        # aproduct.quantity_instock = item.quantity
        # aproduct.save()

    # for item in cart:
    #     item.order_placed= True
    #     item.save()


    context = {
        'shopcart': shopcart,
        'profile': profile
    }
    return render (request, 'ordercompleted.html', context)