from django.db import models

import uuid
from accounts.models import Profile
from datetime import timedelta
from django.utils import timezone
import datetime


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Laptops(BaseModel):
    brand_name = models.CharField(max_length=3000)
    price = models.CharField(max_length=100)
    discription = models.TextField()
    reviews = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name


class Mobiles(BaseModel):
    Product_Name = models.CharField(max_length=100000)
    Product_Price = models.CharField(max_length=100)
    Product_Reviews = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Product_Name)


class Catagory(BaseModel):
    catagory_name = models.CharField(max_length=100,null=True,blank=True)

    def __int__(self):
        return self.uuid


class item(BaseModel):

    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images',null=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0,null=True,blank=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.PROTECT)
    discount_price = models.FloatField(null=True,blank=True)
    description = models.TextField(null=True,blank=True,default=False)
    currency = models.CharField(max_length=100,default='INR')

    def __str__(self):
        return self.title


class Cart(BaseModel):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    items = models.ForeignKey(item,on_delete=models.CASCADE,related_name='orderitem',related_query_name='orderitem')
    quntity = models.IntegerField(default=1)



class order(BaseModel):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    items = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='order',related_query_name='order')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    amount = models.IntegerField(default=0,null=True,blank=True)
    currency = models.CharField(max_length=100,default='INR')

class Adress(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    order_details = models.ForeignKey(order,on_delete=models.CASCADE)
    order_confirmed = models.BooleanField(default=False)



class Amount_transaction(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=300)
    signature = models.CharField(max_length=500)
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)