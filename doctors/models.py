from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)  # Automatically sets the date when created
    availability = models.CharField(max_length=100)  # Example: "10:00 AM - 4:00 PM"
    fees = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 500.00
    password=models.CharField(max_length=100)
    place=models.CharField(max_length=100,default=None)
    status = models.IntegerField(
        default=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(2)
        ]
    )

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"


class Appointments(models.Model):
    date = models.DateField(unique=True)
    appointments = models.JSONField(default=[])


class Booking(models.Model):
    name=models.CharField(max_length=100)
    problem=models.CharField(max_length=100)
    email=models.EmailField(max_length=300)
    address=models.TextField(max_length=500)
    doctor=models.CharField(max_length=100)
    doc_mail=models.EmailField(max_length=300,default="NONE@gmail.com")
    specialization=models.CharField(max_length=100 )
