from logging import exception

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Doctor, Booking, Appointments
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            user = request.POST.get('name')
            password1 = request.POST.get('password')
            data = Doctor.objects.get(email=user)
            if data.status==0:
                if data and password1 == data.password :
                    return render(request,'dashboard.html',{'mail':user})
                else:
                    return HttpResponse("this is wrong data")
            elif data.status==1:
                return HttpResponse("this is rejected by adminstration:")
            else:
                return HttpResponse("this is not approved by adminstration:")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        return HttpResponse("this is posted")
    return render(request, 'login.html')

@csrf_exempt
def booking(request):
    mail=request.POST.get('mail')
    print(mail)
    data=Booking.objects.filter(doc_mail=mail)
    return render(request,'bookingpending.html',{'data':data})
@csrf_exempt
def confirm(request):
    name=request.POST.get('name')
    problem=request.POST.get('problem')
    date=request.POST.get('date')
    email=request.POST.get('email')
    address=request.POST.get('address')
    doctor=request.POST.get('doctor')
    doc_mail=request.POST.get('doc_mail')


    def posting():
        data = Appointments.objects.get(date=date)
        list = data.appointments
        print(f"this is hello kk {data.appointments}")

        j = 0
        for i in list:
            if i["Doctor_Mail"] == doc_mail:
                j = 1
            if j == 1:
                ed = {"Name": name, "problem": problem, "email": email, "address": address, "doctor": doctor,
                      "doc_mail": doc_mail}
                i['application'].append(ed)
                break
        if j == 0:
            ed = {"Doctor_Mail": doc_mail, "application": [
                {"Name": name, "problem": problem, "email": email, "address": address, "doctor": doctor,
                 "doc_mail": doc_mail}]}
            list.append(ed)
        print(list)

        data.appointments = list
        data.save()


    try:

        posting()

    except Exception as e:

        print(e)
        Appointments.objects.create(date=date)

        posting()



    print(name,address,email
          ,doctor,date,doc_mail,problem)
    return HttpResponse("this is approval page")



@csrf_exempt
def shedule(request):
    if request.method == "POST":
        y = request.POST.get('y')
        m = request.POST.get('m')
        d = request.POST.get('d')
        dates =f"{y}-{m}-{d}"

        print(dates)
        da = Appointments.objects.get(date=dates)
        list = da.appointments
        datess = [dates]
        values = []

        for j in list:
            if j["Doctor_Mail"] == request.POST.get('mail'):
                for k in j["application"]:
                    sub = []
                    print(k["Name"], k["problem"])

                    sub.append(k["Name"])
                    sub.append(k["problem"])
                    values.append(sub)
        return render(request, 'shedule.html', {'data': datess, 'va': values})


def dates(request):
    data=Appointments.objects.all()
    return render(request,'dates.html',{'data':data,'mail':request.POST.get('mail')})



