from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Max
import random
from .forms import *

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from order.models import *

# Create your views here.
def home(request):
    home_img = Home.objects.get(pk=1)

    context = {
        'home_img': home_img, 
    }

    return render (request, 'home.html', context)

def training(request):
    training = Training.objects.get(pk=1)
    carousel = Carousel.objects.all()
    prices = Prices.objects.get(category='Training')

    context = {
        'training': training,
        'carousel': carousel,
        'prices': prices,
    }

    return render (request, 'my_training.html', context)

def registerform(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            is_staff = True
            user = authenticate(username = username, password=password)
            login(request, user)

            return redirect ('allproduct')
            # products

        else:
            messages.warning(request, form.errors)
            return redirect('account')

    context = {
        'form': form,
    }

    return render(request, 'account.html', context)

def loginform (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password= password)
        if user:
            login(request,user)
            return redirect('allproduct')
        else:
            messages.info(request, 'Invalid username/password')

    return render(request, 'account.html')

@login_required(login_url='/login')
def logoutfunc(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login')
def profile (request):
    client = User.objects.get(username=request.user.username)
    order = ShopCart.objects.filter(order_placed= True, user=request.user)
    # .exclude(status= 'Completed')

    context = {
        'client': client,
        'order': order,
    }

    return render(request, 'profile.html', context)

@login_required(login_url='/login')
def userupdate (request):
    if request.method == 'POST':
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if profileform.is_valid():

            profileform.save()
            messages.success(request, 'Your Account has been updated.')
            return redirect('profile')
        else:
            messages.warning(request, profileform.errors)
            return redirect('profile')
    return render (request, 'profile.html')

@login_required(login_url='/login')
def userpasswordchange(request):
    form = PasswordChangeForm(request.user, request.POST)

    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successsfully updated')
            return redirect('profile')

        else:
            messages.warning(request, form.errors)
            return redirect ('upchange')

    context = {
        'form': form,
    }
    return render (request, 'userpasswordchange.html', context)

# messages - info, success, warning, error

@login_required(login_url='/login')
def enquires (request):
    user = request.user
    ask = User.objects.get(username = 'askme@admin')
    max_id = Enquires.objects.all().aggregate(max_id = Max("id"))['max_id']
    products = Enquires.objects.all().order_by('id')
    random_product = random.sample(list(products), int(max_id))
    # time_threshold = datetime.now() - timedelta(hours=24)
    # enquires = Enquires.objects.filter(
    #         date_added__range= [
    #         timezone.US(), timezone.now()
    #         ]
    # )
    # enquires = Enquires.objects.filter(date_added= time_threshold)

    now = datetime.now()

    time_threshold = now - timedelta(hours=24)
    # enquires = Enquires.objects.filter(
    #     date_added__range = (time_threshold,now)
    # )
    enquires = Enquires.objects.all()
    adminconvo = Enquires.objects.filter(sender__id=ask.id, receiver= user.id).filter(
        date_added__range = (time_threshold,now)
    )
    userconvo = Enquires.objects.filter(sender__id=user.id, receiver=ask.id).filter(
        date_added__range = (time_threshold,now)
    )
    form = EnquiresForm(request.POST)
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect ('enquires')
        else:
            messages.warning(request, form.errors)
            return redirect ('enquires')

    context = {
        'form': form,
        'ask': ask,
        'enquires': enquires,
        'adminconvo': adminconvo,
        'userconvo': userconvo,
        'random_product': random_product,
    }

    # print(userconvo)
    return render (request, 'make_enquires.html', context)

# def random():
#     max_id = Enquires.objects.all().aggregate(max_id = Max("id"))['max_id']
#     while True:
#         pk = random.randint(1, max_id)
#         product = Enquires.objects.filter(pk=pk).first()
#         if product:
#             return product

# max_id = Products.objects.last().id
# random_id = random.randint(0, max_id)
# random_obj = Products.objects.filter(pk=random_id)

# random.choices(list)

def allproduct (request):
    max_id = Products.objects.exclude(category='Display').aggregate(max_id = Max("id"))['max_id']
    products = Products.objects.exclude(category='Display').order_by('id')
    random_product = random.sample(list(products), int(max_id)-2)

    prices = Products.objects.filter(category='Display')

    context = {
        'allproducts': random_product,
        'prices': prices,
    }

    return render (request, 'products.html', context)

def pendraw (request):
    penprod = Products.objects.filter(category='Pencil Drawings')

    context= {
        'penprod': penprod,
    }

    return render (request, 'pencil_drawing.html', context)

def giftbox (request):
    giftbox = Products.objects.filter(category='Gift Boxes')

    context= {
        'giftbox': giftbox,
    }

    return render (request, 'gift_boxes.html', context)

def greetcard (request):
    greetcard = Products.objects.filter(category='Greeting Cards')

    context= {
        'greetcard': greetcard,
    }

    return render (request, 'greeting_cards.html', context)

def picframe (request):
    picframe = Products.objects.filter(category='Picture Framing')

    context= {
        'picframe': picframe,
    }

    return render (request, 'picture_frames.html', context)

def searchbar (request):
    if request.method == 'GET':
        search = request.GET.get('search')
        pagesearch = Products.objects.filter(description__icontains= search).exclude(category='Display')
        picframe = Products.objects.filter(category='Picture Framing').filter(description__icontains= search)
        giftbox = Products.objects.filter(category='Gift Boxes').filter(description__icontains= search)
        greetcard = Products.objects.filter(category='Greeting Cards').filter(description__icontains= search)
        penprod = Products.objects.filter(category='Pencil Drawings').filter(description__icontains= search)

        context= {
            'search': search,
            'pagesearch': pagesearch,
            'picframe': picframe,
            'giftbox': giftbox,
            'greetcard': greetcard,
            'penprod': penprod,
        }

        return render (request, 'searchbar.html', context)

def prod_det (request, id):
    prod = Products.objects.get(pk = id)

    # max_id = Products.objects.filter(category = prod.category).exclude(id = prod.id).aggregate(max_id = Max("id"))['max_id']
    # products = Products.objects.filter(category = prod.category).exclude(id = prod.id).order_by('id')
    # more = random.sample(list(products), int(max_id))
    more = Products.objects.filter(category = prod.category).exclude(id = prod.id)

    picframe = Products.objects.filter(category='Picture Framing')
    giftbox = Products.objects.filter(category='Gift Boxes').exclude(description__icontains = 'Memory')
    membox = Products.objects.filter(category='Gift Boxes').filter(description__icontains = 'Memory')
    greetcard = Products.objects.filter(category='Greeting Cards')
    penprod = Products.objects.filter(category='Pencil Drawings')

    price = Prices.objects.get(category= prod.category)
    p = Prices.objects.get(category='Greeting Cards')
    price_avg = (p.price1 + p.price2)/2

    context = {
        'prod': prod,
        'price_avg':price_avg,
        'more': more,
        'picframe': picframe,
        'giftbox': giftbox,
        'membox': membox,
        'greetcard': greetcard,
        'penprod': penprod,
        'price': price,
    }

    return render (request, 'prod_det.html', context)