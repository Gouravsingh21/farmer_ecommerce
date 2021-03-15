from django.http import HttpResponse
from django.shortcuts import render,redirect
from  .models import User_acct,User_cart,User_order
from farmer.models import farmer_product as fd

def home (request):
   return render(request,'home.html')

def product(request,product_name):
    prod=fd.objects.filter(product_name=product_name)
    data={'product':prod}
    return render(request,'product.html',data)

def  login(request):
    if request.method=='POST':
        em=request.POST['email']
        pa=request.POST['password']
        sol=User_acct.objects.filter(email=em,password=pa)
        if sol.exists():
            data=fd.objects.all()
            data=list(data)
            data3=[['wheat','farmer/images/wheat.jpg'],['rice','farmer/images/rice.jpg'],['maize','farmer/images/maize.jpg'],['bajra','farmer/images/bazar2.jpeg']]  
            data1={'data2':data3,'status':"this is working perfectly",'range':range(4),'data4':data,'Name':sol[0].Username,'email':sol[0].email,'uid':sol[0].UserId}
            print(data3)
            return render(request,'home.html',data1)
        else:
            status={'status':"You are not register Please Sign Up before"}
            return render(request,'login.html',status)
    else:
        return render(request,'login.html')  

def Signup (request):
    if request.method=='POST':
        user=User_acct()
        user.Username=request.POST['Username']
        user.email=request.POST['Email']
        user.password=request.POST['Password']
        user.save()
        return render(request,'login.html')
    else:
        return render(request,"Signup.html")

def  cart(request, uid,id):
    user=User_acct.objects.filter(UserId=uid)
    uc=User_cart.objects.filter(product=id,user=uid)
    if uc.first() is None:
        product=fd.objects.filter(productId=id)
        um=User_cart()
        um.no_of_product=1
        um.product=product[0]
        um.user=user[0]
        um.save()
    else:
        uc=User_cart.objects.get(product=id,user=uid)
        uc.no_of_product=uc.no_of_product+1
        uc.save()
    data=fd.objects.all()
    data=list(data)
    data3=[['wheat','farmer/images/wheat.jpg'],['rice','farmer/images/rice.jpg'],['maize','farmer/images/maize.jpg'],['bajra','farmer/images/bazar2.jpeg']]  
    data1={'data2':data3,'range':range(4),'data4':data,'Name':user[0].Username,'email':user[0].email,'uid':user[0].UserId}
    return render(request,'home.html',data1)
        
def mycart(request,email):
    myuser=User_acct.objects.filter(email=email)
    cart=User_cart.objects.filter(user=myuser[0])
    amount = 0
    print(cart)
    for index in cart:
        amount=index.product.product_price*index.no_of_product+amount
    data={"mycart":cart,"user":myuser[0],'amount':amount}
    return render(request,'cart.html',data)

def myorder(request,email):
    myuser=User_acct.objects.filter(email=email)
    if request.method=='POST':
        cart=User_cart.objects.filter(user=myuser[0])
        amount = 0
        for index in cart:
            amount=index.product.product_price*index.no_of_product+amount
        uo=User_order()
        uo.address=request.POST['address']
        uo.address1=request.POST['address1']
        uo.city=request.POST['city']
        uo.state=request.POST['state']
        uo.zip_code=request.POST['zip']
        uo.price=amount
        uo.user=myuser[0]
        uo.save()
        for i in cart:
            uo.cart.add(i)
        ord=User_order.objects.filter(user=myuser[0])
        parms={'order':ord,'user':myuser[0]}
        return render(request,'order.html',parms)
    else:
        ord=User_order.objects.filter(user=myuser[0])
        olength=len(ord)-1
        parms={'order':ord,'user':myuser[0],"len":olength}
        return render(request,'order.html',parms)