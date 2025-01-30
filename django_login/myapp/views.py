import bcrypt
from django.shortcuts import render, redirect
from .models import Login
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')

        if not username or not password or not confirm_pass:
            messages.error(request, "All fields are required")
            return redirect('signup')

        if password != confirm_pass:
            messages.error(request, "password does not match")
            return redirect('signup')

        if Login.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('signup')

        # save the data into database
        new_user = Login(username=username, password=password)
        new_user.save()
        messages.success(request, "New user created successfully")
        return redirect('login')
    return render(request, "myapp/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Login.objects.get(username=username)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                request.session["username"] = user.username
                messages.success(request, "Login successful")
                return redirect('index')
            else:
                messages.error(request, "invalid username and password")
        except Login.DoesNotExist:
            messages.error(request, "invalid username and password")
        return redirect('login')
    return render(request, "myapp/login.html")


def index(request):
    if not request.session.get('username'):
        return redirect('login')

    username = request.session.get('username')
    response = render(request, "myapp/index.html", {'username': username})
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def logout_view(request):
    if request.method == 'POST':
        try:
            del request.session['username']
            request.session.flush()
            request.session.set_expiry(3)
        except KeyError:
            pass
        return redirect('login')
    return render(request, 'myapp/logout.html')  # or your logout template
