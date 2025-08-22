from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    # p=Product.objects.all()
    # n=len(p)
    # nSlides=n//4+ceil((n/4)-n//4)
    # params1={"no_of_slides":nSlides,"range":range(1,nSlides),"product":p}
    # allprods=[[p,range(1,nSlides),nSlides],[p,range(1,nSlides),nSlides]]
    
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-n//4)
        allprods.append([prod,range(1,nSlides),nSlides])
    
    params2={'allprods':allprods}

    return render(request,'Shop/index.html',params2)

def About(request):
    return render(request,"Shop/about.html")
def Contact(request):
    return HttpResponse("Contact")
def Tracker(request):
    return HttpResponse("Tracker")
def Search(request):
    return HttpResponse("Search")
def ProductView(request):
    return HttpResponse("ProductView")
def Checkout(request):
    return HttpResponse("Checkout")

