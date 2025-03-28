from logging import exception

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Doctor,Booking
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




@csrf_exempt
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        specialization = request.POST['specialization']
        phone = request.POST['phone']
        email = request.POST['email']
        availability = request.POST['availability']
        fees = request.POST['fees']
        password=request.POST['password']
        place=request.POST['place']

        # Save to database
        Doctor.objects.create(
            name=name,
            specialization=specialization,
            phone=phone,
            email=email,
            availability=availability,
            fees=fees,
            password=password,
            place=place

        )

        return render(request, 'register_doctor.html') # Redirect to a success page

    return render(request, 'register_doctor.html')






# views.py

# views.py

import random
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    return str(random.randint(100000, 999999))  # Generates a random 6-digit OTP

@csrf_exempt
def send_email_view(request):

    if request.method == "POST":
        doc = request.POST.get('doctor')
        doc_mail=request.POST.get('email')
        spe=request.POST.get('spe')


    if request.method == 'POST' and request.POST.get("app") != "appointment":
        name = request.POST.get('name')
        receiver_email = request.POST.get('receiver_email')
        problem=request.POST.get('problem')
        specialization = request.POST.get('specialization')
        address = request.POST.get('address')
        doctor = request.POST.get("doctor")
        doc_mail=request.POST.get('doc_mail')
        spe=request.POST.get('spe')

        # Generate OTP
        otp = generate_otp()

        # Prepare email content
        subject = f"Verificatiion for Doctor Appointment - Your OTP"
        message = f"""
        Hi {name} ,this otp verification for doctor appointment  of your booking 
        Name: {name}
        Specialization: {spe}
        Problem: {problem}
        OTP: This is otp for Book Appointments:  {otp}
        Address: {address}
        Thanking you,
        
        """

        # Send the email
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [receiver_email],
            fail_silently=False,
        )

        return render(request, 'send_email.html', {'otp': otp ,'name':name,'problem':problem,
                                                   'mail':receiver_email,'address':address,'specialization':specialization,
                                                "doctor":doctor, "doc_mail":doc_mail,"spe":spe})  # Pass OTP to success page for display
    return render(request, 'send_email.html',{"doctor":doc , "doc_mail":doc_mail ,"spe":spe})  # Render the form if GET request


@csrf_exempt
def verify(request):
    try:
        if request.method=="POST":
            veotp=request.POST.get('veotp')
            otp=request.POST.get('otp')
            print(request.POST.get('spe'))
            if veotp == otp:
                Booking.objects.create(name=request.POST.get('name'),
                                       problem=request.POST.get('problem'),
                                       email=request.POST.get('mail'),
                                       address=request.POST.get('address'),
                                       doctor=request.POST.get('doctor'),
                                       doc_mail=request.POST.get('doc_mail'),
                                       specialization=request.POST.get('spe'))
                return render(request,'login.html')
            else:
                return HttpResponse('Password is incorrect')
    except Exception as e:
        print("this is error")
        return HttpResponse(f"this is error {e}")








