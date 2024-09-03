from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Payment(models.Model):
    amount = models.FloatField()
    paid_date = models.DateField()
    channel = models.CharField(max_length=20)
    paid_to = models.ForeignKey(User, on_delete=models.CASCADE)

