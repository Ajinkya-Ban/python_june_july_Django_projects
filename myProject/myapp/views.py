from django.shortcuts import render, redirect
from .models import Contact, Register


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

        Contact.objects.create(fname=fname, lname=lname, mobile=mobile, email=email, message=message)
        return render(request, "myapp/success.html")
    return redirect(request, "myapp/contact.html")


def submit_register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        address = request.POST.get("add")
        country = request.POST.get("country")  # Get selected country value
        state = request.POST.get("state")      # Get selected state value
        city = request.POST.get("city")        # Get selected city value
        profile_image = request.FILES.get("profile_image")

        # Save all the form values, including the selected ones, to the database
        Register.objects.create(
            fullname=fullname,
            mobile=mobile,
            email=email,
            address=address,
            country=country,
            state=state,
            city=city,
            profile_image=profile_image
        )
        return render(request, "myapp/success.html")
    return render(request, "myapp/register.html")

