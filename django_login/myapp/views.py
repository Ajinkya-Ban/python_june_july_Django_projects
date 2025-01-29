import bcrypt
from django.shortcuts import render,redirect
from .models import Login
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')

        if not username or not password or not confirm_pass:
            messages.error(request,"All fields are required")
            return redirect('signup')

        if password != confirm_pass:
            messages.error(request,"password does not match")
            return redirect('signup')

        if Login.objects.filter(username=username).exists():
            messages.error(request,"Username already taken")
            return redirect('signup')

        # save the data into database
        new_user = Login(username=username, password=password)
        new_user.save()
        messages.success(request,"New user created successfully")
        return redirect('login')
    return render(request,"myapp/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Login.objects.get(username=username)

            if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                request.session["username"] = user.username
                messages.success(request,"Login successful")
                return redirect('index')
            else:
                messages.error(request,"invalid username and password")
        except Login.DoesNotExist:
            messages.error(request,"invalid username and password")
        return redirect('login')
    return render(request,"myapp/login.html")

def index(request):
    username = request.session.get('username')
    if username:
        return render(request,"myapp/index.html", {'username': username}) # Corrected line
    else:
        messages.error(request,"You need login first")
        return redirect('login')

def logout_view(request):

    request.session.flush()
    messages.success(request, "Logged out successfully")
    return redirect("login")