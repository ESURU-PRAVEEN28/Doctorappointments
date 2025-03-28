from django.contrib import admin
from .models import Doctor, Appointments,Booking


class Doc(admin.ModelAdmin):
    list_display = ("name","specialization")
    list_filter = ("specialization",)


class App(admin.ModelAdmin):
    list_display = ["date", "appointments"]

class Book(admin.ModelAdmin):
    list_display = ["name", "problem","doctor"]

admin.site.register(Doctor,Doc)
admin.site.register(Appointments, App)
admin.site.register(Booking,Book)