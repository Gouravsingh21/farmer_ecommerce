from django.contrib import admin

# Register your models here.
from Food.models import User_acct,User_delivery,User_order,User_cart

admin.site.register(User_acct)
admin.site.register(User_cart)
admin.site.register(User_delivery)
admin.site.register(User_order)