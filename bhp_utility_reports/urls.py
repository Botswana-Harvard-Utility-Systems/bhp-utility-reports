"""bhp_utility_reports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import (HomeView, 
                    EmployeeListBoardView,  
                    EmployeeTimesheetReportListboardView,
                    DepartmentsTimesheetReportListboardView)
from .patterns import identifier
from edc_dashboard import UrlConfig


app_name = 'bhp_utility_reports'


employees_listboard_url_config = UrlConfig(
    url_name='employees_report_listboard_url',
    view_class=EmployeeListBoardView,
    label='employee_listboard',)

    
timesheet_listboard_url_config = UrlConfig(
    url_name='employee_timesheet_report_listboard_url',
    view_class=EmployeeTimesheetReportListboardView,
    label='timesheet_listboard',)


departments_listboard_url_config = UrlConfig(
    url_name='departments_timesheet_report_listboard_url',
    view_class=DepartmentsTimesheetReportListboardView,
    label='departments_timesheet_listboard',)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='bhp_utility_reports_home_url',),
    # path('employee_listboard/<page>', EmployeeListBoardView.as_view(),
    #      name='employees_report_listboard_url',),
]

urlpatterns += employees_listboard_url_config.listboard_urls
urlpatterns += timesheet_listboard_url_config.listboard_urls
urlpatterns += departments_listboard_url_config.listboard_urls

