from .models import Doctor, Booking
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from logging import exception


@csrf_exempt
def approve(request):
    data = Doctor.objects.filter(status=2)
    # print(data)
    return render(request, 'aproving.html',{'data':data})

@csrf_exempt
def approvedoctor(request):
    if request.method=="POST":
        mail=request.POST.get('mail')
        data=Doctor.objects.get(email=mail)
        data.status=0
        data.save()
        return redirect('approve')



@csrf_exempt
@login_required
def reject(request):
    if request.method=="POST":
        data=Doctor.objects.get(email=request.POST.get('mail'))
        data.status=1
        data.save()
        return redirect('approve')