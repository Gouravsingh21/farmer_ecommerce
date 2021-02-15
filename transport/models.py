from django.db import models

# Create your models here.
class transport(models.Model):
    AgencyId=models.AutoField(primary_key=True)
    Aname=models.CharField(max_length=30)
    mobile=models.IntegerField()
    address=models.CharField(max_length=50)
    email=models.EmailField(null=True)
    pincode=models.IntegerField()

    def __str__(self):
        return self.fname

class delivery(models.Model):
    deliveryId=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=20)
    pickup_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    delivery_status=models.CharField(max_length=20)
    AgencyId=models.IntegerField()
    delboyId=models.IntegerField()

class delperson(models.Model):
    delboyId=models.AutoField(primary_key=True)    
    delboyname=models.CharField(max_length=20)
    AgencyId=models.IntegerField()

    def  __str__(self):
        return self.delboyname
    