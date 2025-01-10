from django.shortcuts import render, redirect
from .models import Contact, Register
from django.core.exceptions import ValidationError


# Create your views here.
def getHomePage(request):
    users = Register.objects.all()
    return render(request, 'myapp/home.html', {'users': users})


def getRegisterPage(request):
    users = Register.objects.all()
    return render(request, "myapp/register.html",{'users':users})


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
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        address = request.POST.get("add")
        country = request.POST.get("country")  # Get selected country value
        state = request.POST.get("state")  # Get selected state value
        city = request.POST.get("city")  # Get selected city value
        profile_image = request.FILES.get("profile_image")

        # Save all the form values, including the selected ones, to the database
        register = Register(
            fullname=fullname.title(),
            gender=gender,
            mobile=mobile,
            email=email,
            address=address,
            country=country,
            state=state,
            city=city,
            profile_image=profile_image
        )
        try:
            register.save()
            return render(request, "myapp/success.html")

        except ValidationError as err:
            return render(request, "myapp/register.html", {
                "error": err.message_dict,
                "data": request.POST
            })
    return render(request, "myapp/register.html")

def edit_user(request,id):
    pass

def delete_user(request,user_id):
    user = Register.objects.get(id=user_id)
    getAllUser = Register.objects.all()
    user.delete()
    return redirect('register')

