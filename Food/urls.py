from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('product/<str:product_name>',views.product,name='product'),
    path('login',views.login,name='login'),
    path('Signup',views.Signup,name='Signup'),
    path('cart/<int:uid>/<int:id>',views.cart,name='cart'),
    path('mycart/<str:email>',views.mycart,name='mycart'),
    path('myorder/<str:email>',views.myorder,name='myorder'),
  ]
