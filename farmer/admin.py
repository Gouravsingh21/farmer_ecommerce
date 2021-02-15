from django.contrib import admin

# Register your models here.

from farmer.models import farmer_info,farmer_product
admin.site.register(farmer_info)
admin.site.register(farmer_product)