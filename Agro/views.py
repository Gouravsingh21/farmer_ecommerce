from django.http import HttpResponse
from django.shortcuts import render 
from farmer.models import farmer_product


def index(request):
    data=farmer_product.objects.all()
    data=list(data)
    data3=[['wheat','farmer/images/wheat.jpg'],['rice','farmer/images/rice.jpg'],['maize','farmer/images/maize.jpg'],['bajra','farmer/images/bazar2.jpeg']]  
    data1={'data2':data3,'status':"this is working perfectly",'range':range(4),'data4':data}
    return render(request,'index.html',data1)
    
def about(request):
    return render(request,"about.html")

def project(request):
    return render(request,'project.html')

def  contact(request):
    return render(request,"contact.html")