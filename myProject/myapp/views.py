from django.shortcuts import render


# Create your views here.
def getHomePage(request):
    return render(request, "myapp/home.html")

def getRegisterPage(request):
    return render(request,"myapp/register.html")

def getProductPage(request):
    return render(request, "myapp/products.html")

def getContactPage(request):
    return render(request,"myapp/contact.html")