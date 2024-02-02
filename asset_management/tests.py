from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company, Employee, Device

# Company models creation test
class CompanyModelTest(TestCase):
    def test_company_str_method(self):
        company = Company.objects.create(name='Test Company')
        self.assertEqual(str(company), 'Test Company')

# Employee models creation test
class EmployeeModelTest(TestCase):
    def test_employee_str_method(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        employee = Employee.objects.create(user=user, company=Company.objects.create(name='Test Company'))
        self.assertEqual(str(employee), 'testuser')

# Device models creation test
class DeviceModelTest(TestCase):
    def test_device_str_method(self):
        device = Device.objects.create(name='Test Device', company=Company.objects.create(name='Test Company'))
        self.assertEqual(str(device), 'Test Device')


