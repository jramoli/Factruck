"""Factruck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Factruck.views import *
from Factura.views import *

from Factruck.views import *
from Factura.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', view_login, name='login'),
    path('logout/', view_logout, name='logout'),
    path('factura/', view_html_factura, name='factura'),
    path('', view_pdf_factura, name='factura_pdf'),
    path('factura_simple/', view_html_factura_simple, name='factura_simple'),
    path('factura_simple_pdf/', view_pdf_factura_simple, name='factura_simple_pdf'),
]
