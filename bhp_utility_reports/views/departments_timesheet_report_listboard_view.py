from os import stat
import pdb
from bhp_personnel.models.department import Department
from django.apps import registry
from django.contrib.auth.mixins import LoginRequiredMixin
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.listboard_filter import ListboardViewFilters
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from ..model_wrappers import TimesheetModelWrapper
import re
import six
from django.db.models import Q
from ..filters import DepartmentListboardViewFilters
from urllib.parse import urljoin, parse_qsl, urlencode, unquote
from collections import deque


class DepartmentsTimesheetReportListboardView(NavbarViewMixin,
                            EdcBaseViewMixin,
                            SearchFormViewMixin,
                            ListboardView,
                            ListboardViewFilters):

    listboard_template = 'departments_timesheet_report_listboard_template'
    listboard_url = 'departments_timesheet_report_listboard_url'
    listboard_panel_style = 'info'
    # listboard_fa_icon = "fa-user-plus"
    listboard_view_filters = DepartmentListboardViewFilters()
    navbar_name = 'bhp_utility_reports'
    model = 'timesheet.monthlyentry'
    model_wrapper_cls = TimesheetModelWrapper
    search_form_url = 'departments_timesheet_report_listboard_url'
    paginate_by = 10


    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['departments'] = Department.objects.values_list('dept_name')
        context['statuses'] = ('new', 'submitted', 'approved', 'rejected', 'verified')
        # context['querystring'] = 'tettegghbshbaugsgausyauyh'

        last_selected_department = self.request.GET.get('department', None)
        last_selected_status = self.request.GET.get('status', None)
        last_start_date = self.request.GET.get('end_date', None)
        last_end_date = self.request.GET.get('start_date', None)

        query_parameters = deque()

        if last_selected_department and last_selected_department != 'all':
            context['last_selected_department'] = last_selected_department
            query_parameters.append(f'department={last_selected_department.replace("&", "%26")}')

        if last_selected_status and last_selected_status != 'all':
            context['last_selected_status'] = last_selected_status
            query_parameters.append(f'status={last_selected_status}')

        if last_start_date:
            context['last_start_date'] = last_start_date
            query_parameters.append(f'start_date={last_start_date}')

        if last_end_date:
            context['last_end_date'] = last_end_date
            query_parameters.append(f'end_date={last_end_date}')

        querystring = f"just_a_placeholder?{'&'.join(query_parameters)}"

        # import pdb; pdb.set_trace()


        context['querystring'] = querystring

        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)

        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        department = self.request.GET.get('department', None)
        status = self.request.GET.get('status', None)
        date_fields = ['submitted_datetime', 'approved_date',
                       'verified_date', 'rejected_date', 'created']


        if department and department != 'all':
            options.update({'employee__department__dept_name': department})


        if status and status != 'all':
            options.update({'status': status})


        if start_date:
            for date_field in date_fields:
                options.update({f'{date_field}__gte': start_date})

        elif end_date:
            for date_field in date_fields:
                options.update({f'{date_field}__lte': start_date})

        elif start_date and end_date:
            for date_field in date_fields:
                options.update({f'{date_field}__range': [start_date, end_date]})

        return options

    def extra_search_options(self, search_term):
        q = Q()

        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        
        if re.match(email_regex, search_term):
            q = Q(employee__email = search_term)

        return q

