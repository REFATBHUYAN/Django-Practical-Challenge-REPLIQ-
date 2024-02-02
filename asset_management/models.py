from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.user.username

class Device(models.Model):
    name = models.CharField(max_length=100)
    checkout_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.TextField(null=True, blank=True)
    condition_on_return = models.TextField(null=True, blank=True)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_devices')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices')

    def __str__(self):
        return self.name
