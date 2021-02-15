from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.farmer,name="farmer"),
    path('farlogin',views.farlogin,name="farlogin"),
    path('farhome',views.farmer_home,name='fhome'),
]
