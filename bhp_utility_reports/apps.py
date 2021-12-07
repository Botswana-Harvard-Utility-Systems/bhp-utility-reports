
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'bhp_utility_reports'
    verbose_name = 'BHP Utility Reports'
    admin_site_name = 'bhp_utility_reports_admin'
    extra_assignee_choices = ()
    assignable_users_group = 'assignable users'

    def ready(self):
        pass
