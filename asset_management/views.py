from rest_framework import generics
from .models import Company, Employee, Device
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer




