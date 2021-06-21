from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    symptoms = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    doc = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    pat = models.ForeignKey(Patient,on_delete=models.CASCADE)

