from django.urls import path,include
from .views import register,send_email_view,verify
from .loginpage import admin_login
from .approving import approve,approvedoctor,reject
from .doctordashboard import login,booking,confirm,shedule,dates,rejecting
from .home import home,master

urlpatterns=[

    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('send-email/', send_email_view, name='send_email'),
    path('verify/',verify,name="verify"),
    path('home/',home,name="home"),
    path('approve/',approve,name="approve"),
    path('approvedoctor/',approvedoctor,name="approvedoctor"),
    path('reject/',reject,name="reject"),
    path('admin_login/',admin_login,name="admin_login"),
    path('booking/',booking,name="booking"),
    path('confirm/',confirm,name="confirm"),
    path('shedule/',shedule,name="shedule"),
    path('dates/',dates,name="dates"),
    path('rejecting/',rejecting,name="rejecting"),
    path('',master,name="master")
]