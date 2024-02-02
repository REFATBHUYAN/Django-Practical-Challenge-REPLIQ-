"""
URL configuration for asset_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# below code is added for creating automated api documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Corporate Assets Tracker API",
      default_version='v1',
      description="Django app to track corporate assets such as phones, tablets, laptops and other gears handed out to employees.",
      terms_of_service="http://127.0.0.1:8000/api/terms/",
      contact=openapi.Contact(email="refatbubt@gmail.com"),
      license=openapi.License(name="Tracker License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# here also imported app urls file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('asset_management.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
