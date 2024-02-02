from django.urls import path
from .views import (
    CompanyListCreateView, CompanyRetrieveUpdateDeleteView,
    EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView,
    DeviceListCreateView, DeviceRetrieveUpdateDeleteView
)

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDeleteView.as_view(), name='company-retrieve-update-delete'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-retrieve-update-delete'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDeleteView.as_view(), name='device-retrieve-update-delete'),
]
