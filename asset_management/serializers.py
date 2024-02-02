from rest_framework import serializers
from .models import Company, Employee, Device


# Company serilization code to make python object model to json formate
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# Employee serilization code to make python object model to json formate
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Device serilization code to make python object model to json formate
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


