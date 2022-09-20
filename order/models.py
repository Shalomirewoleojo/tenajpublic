from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from home.models import Products
from django.utils.safestring import mark_safe
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=15)
    city = models.CharField(blank=True, max_length=15)
    state = models.CharField(blank=True, max_length=15)
    country = models.CharField(blank=True, max_length=15)
    zipcode = models.CharField(blank=True, max_length=15)
    image = models.ImageField(blank=True, null=True, upload_to='images/users/', default='defaultpic.jpg')

    def __str__(self):
        return self.user.username

    
    @property
    def username(self):
        if self.user_id is not None:
            return self.user.first_name+ ' ' + self.user.last_name + '[' + self.user.username + ']'


    @property
    def email(self):
        if self.user_id is not None:
            return (self.user.email)

    def image_tag(self):
        return mark_safe('<img scr="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    class Meta:
        db_table = 'userprofile'
        managed = True
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

class ShopCart (models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete = models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    size = models.CharField(max_length=20)
    order_code = models.CharField(max_length=70, editable=False)
    order_placed = models.BooleanField(default=False)
    specification = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.product.category

    @property
    def amount(self):
        return self.price * self.quantity

class TrainingPurchase (models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    price = models.FloatField()
    course = models.CharField(max_length=20)
    order_code = models.CharField(max_length=70, editable=False)
    order_placed = models.BooleanField(default=False)

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = models.FloatField(null=True, blank=True)
    order_placed = models.BooleanField(default=False)
    order_code = models.CharField(max_length=70, editable=False)
    payment_code = models.CharField(max_length=8, editable=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField (blank=True, null=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    adminnote = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.user.username
        # return self.user.UsernameField
