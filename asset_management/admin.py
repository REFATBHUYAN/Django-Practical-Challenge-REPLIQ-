from django.contrib import admin
from .models import Company, Employee, Device


#resgister database site to admin
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)