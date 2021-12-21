

from django.apps import apps as django_apps
from django.contrib.sites.models import Site
from django.core import paginator
from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
from bhp_personnel.models import Employee, Department, Supervisor, department
from django.core.paginator import Paginator


class HomeView(NavbarViewMixin, EdcBaseViewMixin, TemplateView):
    template_name = 'bhp_utility_reports/home.html'
    navbar_name = 'bhp_utility_reports'
    navbar_selected_item = 'Reports'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_totals())
        context.update(self.get_department_statistics())

        return context

    def get_totals(self):

        statistics = dict()

        statistics['total_employees'] = Employee.objects.count()
        statistics['total_departments'] = Department.objects.count()
        statistics['total_supervisors'] = Supervisor.objects.count()

        return statistics

    def get_department_statistics(self):

        context = dict()
        departments = Department.objects.all()
        page_number = self.request.GET.get('page_number', 1)
        departments_paginator = Paginator(departments, 10)
        department_page = departments_paginator.page(page_number)

        statistics = []

        for department in department_page.object_list:

            department_stat = dict()
            department_stat['dept_name'] = department.dept_name
            department_stat['dept_total_employees'] = department.employee_set.count()
            department_stat['dept_percentage'] = round((department_stat['dept_total_employees'] /
                                                        Employee.objects.count()) * 100, 1)
            statistics.append(department_stat)

        context['department_statistics'] = statistics
        context['department_statistics_page'] = department_page.next_page_number()
        context['department_statistics_range'] = departments_paginator.page_range

        return context
