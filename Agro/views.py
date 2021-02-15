from django.http import HttpResponse
from django.shortcuts import render 
from farmer.models import farmer_product


def index(request):
    data=farmer_product.objects.all()
    data=list(data)
    # data3 = [data[i * 4:(i + 1) * 4] for i in range((len(data) + 4 - 1) // 4 )]
    data3=[['wheat','farmer/images/wheat.jpg'],['rice','farmer/images/rice.jpg'],['maize','farmer/images/maize.jpg'],['bajra','farmer/images/bazar2.jpeg']]  
    data1={'data2':data3,'status':"this is working perfectly",'range':range(4),'data4':data}
    return render(request,'index.html',data1)
    
