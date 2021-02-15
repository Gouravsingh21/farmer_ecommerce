from django.contrib import admin

# Register your models here.
from transport.models import transport,delivery,delperson
admin.site.register(transport)
admin.site.register(delivery)
admin.site.register(delperson)