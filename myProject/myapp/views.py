from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def getHomePage(request):
    return render(request, "myapp/home.html")


def getRegisterPage(request):
    return render(request, "myapp/register.html")


def getProductPage(request):
    return render(request, "myapp/products.html")


def getContactPage(request):
    return render(request, "myapp/contact.html")


def submit_contact(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        mobile = request.POST.get("mob")
        email = request.POST.get("email")
        message = request.POST.get("msg")

        Contact.objects.create(fname=fname,lname=lname,mobile=mobile,email=email,message=message)
        return render(request, "myapp/success.html")
    return redirect(request,"myapp/contact.html")


