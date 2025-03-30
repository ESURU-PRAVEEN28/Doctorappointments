from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('approve')  # Redirect to Django Admin
        else:
            messages.error(request, "Invalid credentials or not an admin.")

    return render(request, "admin/loginpage.html")

def logout(request):
    del request.session['d']
    del request.session['gana']
    return render(request,"doctorlogin/logout_success.html")