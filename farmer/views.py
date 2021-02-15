from django.shortcuts import render
from django.http import HttpResponse
from .models import farmer_info as farm,farmer_product as pd
# Create your views here.

def farmer(request):
        if request.method=='POST':
                f=farm()
                f.fname=request.POST['name']
                f.village=request.POST['vill_name']
                f.distirct=request.POST['dist_name']
                f.address=request.POST['address']
                f.aadhar_no=request.POST['addhar']
                f.email=request.POST['email']
                f.mobile=request.POST['phone']
                f.password=request.POST['password']
                f.save()
                state={'status1':"Farmer register successfully You can login now!!!"}
                return render(request,'farlogin.html',state)
        else:
             return render(request,'farmer.html')

def farlogin(request):
        a=1
        if request.method=='POST':
                em=request.POST['mobile']
                pa=request.POST['password']
                em=int(em)
                sol=farm.objects.all()
                for i in range(0,len(sol)):
                        if sol[i].mobile==em and  sol[i].password==pa:
                                # print(sol[i].email,sol[i].Username)
                                a=0
                                break
                        else:
                                a=1
                if a==0:
                        print('user correct')
                        data={'Name':sol[i].fname,'email':sol[i].mobile,'data1':sol[i]}
                        return render(request,'farhome.html',data)
                else:
                        print('user incorrect')
                        status={'status':"You are not register Please Sign Up before"}
                        return render(request,'farlogin.html',status)  
        else:
                print('login page')
                return render(request,'farlogin.html')


def farmer_home(request):
        if request.method=='POST':
                p=pd()
                mob=request.POST['mobile']
                fam=farm.objects.get(mobile=int(mob))
                p.product_name=request.POST['prodname']
                p.product_rating=request.POST['prodrating']
                p.product_special=request.POST['prodspecial']
                p.product_type=request.POST['prodtype']
                p.product_price=request.POST['prodprice']
                p.product_image=request.POST['prodimage']
                p.farmer=fam
                p.save()
                sta={'s':"Crop Added succesfully add more crops now"}
                return render(request,'farhome.html',sta)
        else:
                return render(request,'farhome.html')