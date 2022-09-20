from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Home (models.Model):
    first_img = models.ImageField(upload_to = 'images/')
    pencil_drawing = models.ImageField(upload_to = 'images/')
    picture_framing = models.ImageField(upload_to = 'images/')
    gift_box = models.ImageField(upload_to = 'images/')
    greeting_card = models.ImageField(upload_to = 'images/')
    training = models.ImageField(upload_to = 'images/')
    appears = models.ImageField(upload_to = 'images/')
    review1 = models.ImageField(upload_to = 'images/')
    review2 = models.ImageField(upload_to = 'images/')
    review3 = models.ImageField(upload_to = 'images/')
    review4 = models.ImageField(upload_to = 'images/')

class Training (models.Model):
    beginners = models.ImageField(upload_to = 'images/')
    intermediate = models.ImageField(upload_to = 'images/')
    advanced = models.ImageField(upload_to = 'images/')
    t_video = models.FileField(upload_to = 'files/')
    carousel = models.ImageField(upload_to = 'images/', blank=True, null=True)

class Carousel(models.Model):
    carousel = models.ImageField(upload_to = 'images/')

class Enquires(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientenquiry')
    question = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    time_added = models.TimeField(auto_now_add = True, null=True, blank=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.receiver, self.sender)

class Products (models.Model):
    CATEGORY = (
        ('Pencil Drawings', 'Pencil Drawings'),
        ('Picture Framing', 'Picture Framing'),
        ('Gift Boxes', 'Gift Boxes'),
        ('Greeting Cards', 'Greeting Cards'),
        ('Display', 'Display'),
    )
    category = models.CharField(choices=CATEGORY,  max_length=30)
    img= models.ImageField(upload_to = 'images/') 
    description = models.CharField(max_length=200, default='giftbox') 
    
class Prices (models.Model):
    CATEGORY = (
        ('Pencil Drawings', 'Pencil Drawings'),
        ('Picture Framing', 'Picture Framing'),
        ('Gift Boxes', 'Gift Boxes'),
        ('Greeting Cards', 'Greeting Cards'),
        ('Training', 'Training'),
    )
    category = models.CharField(choices=CATEGORY,  max_length=30)
    price1 = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    price3 = models.FloatField(blank=True, null=True)
    price4 = models.FloatField(blank=True, null=True)
    price5 = models.FloatField(blank=True, null=True)
    price6 = models.FloatField(blank=True, null=True)