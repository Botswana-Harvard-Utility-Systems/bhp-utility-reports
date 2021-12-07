from django.contrib.auth.mixins import LoginRequiredMixin
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from ..model_wrappers import EmployeeModelWrapper
from ..filters import EmployeeListboardViewFilters
import re
from django.db.models import Q
from bhp_personnel.models import Department

class EmployeeListBoardView(NavbarViewMixin,
                            EdcBaseViewMixin,
                            ListboardFilterViewMixin,
                            SearchFormViewMixin,
                            ListboardView):

    listboard_template = 'employees_report_listboard_template'
    listboard_url = 'employees_report_listboard_url'
    listboard_panel_style = 'info'
    # listboard_fa_icon = "fa-user-plus"
    # listboard_view_filters = EmployeeListboardViewFilters()
    navbar_name = 'bhp_utility_reports'
    model = 'bhp_personnel.employee'
    model_wrapper_cls = EmployeeModelWrapper
    search_form_url = 'employees_report_listboard_url'
    ordering = 'hired_date'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.values_list('dept_name')
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        return options

    def get_queryset_exclude_options(self, request, *args, **kwargs):
        """Returns exclude options applied to every
        queryset.
        """
        return {}

    # def extra_search_options(self, search_term):
    #     q = Q()
    #     return q
