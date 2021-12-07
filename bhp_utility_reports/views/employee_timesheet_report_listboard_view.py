from django.apps import registry
from django.contrib.auth.mixins import LoginRequiredMixin
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from ..model_wrappers import TimesheetModelWrapper
import re
from django.db.models import Q

class EmployeeTimesheetReportListboardView(NavbarViewMixin,
                            EdcBaseViewMixin,
                            ListboardFilterViewMixin,
                            SearchFormViewMixin,
                            ListboardView):

    listboard_template = 'employee_timesheet_report_listboard_template'
    listboard_url = 'employee_timesheet_report_listboard_url'
    listboard_panel_style = 'info'
    # listboard_fa_icon = "fa-user-plus"
    navbar_name = 'bhp_utility_reports'
    model = 'timesheet.monthlyentry'
    model_wrapper_cls = TimesheetModelWrapper
    search_form_url = 'employee_timesheet_report_listboard_url'
    paginate_by = 100

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        return options

    def extra_search_options(self, search_term):
        q = Q()

        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        
        if re.match(email_regex, search_term):
            q = Q(employee__email = search_term)

        return q

