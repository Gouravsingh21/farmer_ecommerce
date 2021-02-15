from django.shortcuts import render

# Create your views here.

def transport(request):
    return render(request,'transport.html')
