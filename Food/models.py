from django.db import models
from farmer.models import farmer_product
# Create your models here.
#There is my table for the database

class User_acct(models.Model):
    UserId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=30,null=False)
    email = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=30)
    mobile=models.IntegerField(null=True)
    Date = models.DateField(auto_now=True)

    def __str__(self):
        return self.Username


class User_cart(models.Model):
    cartId=models.AutoField(primary_key=True)
    no_of_product=models.IntegerField()
    product=models.ForeignKey(farmer_product,on_delete=models.CASCADE,default=None)
    user=models.ForeignKey(User_acct,on_delete=models.CASCADE,default=None)
    

class User_order(models.Model):
    orderId=models.AutoField(primary_key=True)
    cart=models.ManyToManyField(User_cart)
    user=models.ForeignKey(User_acct,on_delete=models.CASCADE)
    orderdt=models.DateTimeField(auto_now=True)
    price=models.IntegerField(null=True)
    address=models.CharField(default='',max_length=50)
    address1=models.CharField(default='',max_length=50)
    state=models.CharField(default='',max_length=20)
    city=models.CharField(default='',max_length=20)
    zip_code=models.IntegerField()


class User_delivery(models.Model):
    deliveryId=models.AutoField(primary_key=True)
    deliverydt=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User_acct,on_delete=models.CASCADE)
    order=models.ForeignKey(User_order,on_delete=models.CASCADE)    

