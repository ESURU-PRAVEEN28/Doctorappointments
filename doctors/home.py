from .models import Doctor, Booking
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from logging import exception

@csrf_exempt
def home(request):
    data = Doctor.objects.filter(status=0)
    # d=User.objects.create_user(username="gana123",password="gana123",is_staff=True)
    print(data)
    return render(request,'home.html',{'data':data})