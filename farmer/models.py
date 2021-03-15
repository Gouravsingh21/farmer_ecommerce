from django.db import models

# Create your models here.
class farmer_info(models.Model):
    farmerId=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=30,default="")
    mobile=models.IntegerField(unique=True)
    village=models.CharField(max_length=50)
    distirct=models.CharField(max_length=30)
    email=models.EmailField(null=True,default="")
    aadhar_no=models.IntegerField()
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=20,default='')

    def __str__(self):
        return self.fname
    
class farmer_product(models.Model):
    productId=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=20)
    product_special=models.TextField()
    product_type=models.CharField(max_length=20)
    product_rating=models.IntegerField(default=3)
    register_date=models.DateField(auto_now=True)
    farmer=models.ForeignKey(farmer_info,on_delete=models.CASCADE)
    product_price=models.IntegerField(default='1000')
    product_image=models.ImageField(upload_to='media/farmer/images',default='')

    def  __str__(self):
        return self.product_name
    