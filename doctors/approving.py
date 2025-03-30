from .models import Doctor, Booking
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from logging import exception
from .views import emailmessage


@csrf_exempt
def approve(request):
    data = Doctor.objects.filter(status=2)
    # print(data)
    return render(request, 'admin/aproving.html',{'data':data})

@csrf_exempt
def approvedoctor(request):
    if request.method=="POST":
        mail=request.POST.get('mail')
        data=Doctor.objects.get(email=mail)
        data.status=0
        data.save()
        subject = f"confirming for Doctor registration"
        message = f"""
                Hi {data.name} ,this otp verification for doctor appointment  of your booking 
                Name: {data.name}
                Specialization: {data.specialization}
                Email: {data.email}
                Address: {data.place}
                You may access ur account as your convinent for all over global doctor appointments
                Thanking you,

                """
        try:
            emailmessage(subject,message,mail)
        except Exception as e:
            print(e)



        return redirect('approve')



@csrf_exempt
@login_required
def reject(request):
    if request.method=="POST":
        mail=request.POST.get('mail')
        data=Doctor.objects.get(email=request.POST.get('mail'))
        data.status=1
        data.save()
        subject = f"Rejected for Doctor registration"
        message = f"""
                        Hi {data.name} ,this Rejected for doctor appointment application  of your booking 
                        Name: {data.name}
                        Specialization: {data.specialization}
                        Email: {data.email}
                        Address: {data.place}
                        You maynot be access ur account as your convinent for all over global doctor appointments
                        Thanking you,

                        """
        try:
            emailmessage(subject, message, mail)
        except Exception as e:
            print(e)
        return redirect('approve')