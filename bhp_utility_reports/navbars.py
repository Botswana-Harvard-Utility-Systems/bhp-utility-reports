from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


bhp_utility_navbar = Navbar(name='bhp_utility_reports')

no_url_namespace = True if settings.APP_NAME == 'bhp_utility_reports' else False

bhp_utility_navbar.append_item(
    NavbarItem(name='reports',
               label='General Reports',
               fa_icon='fa-cogs',
               url_name='bhp_utility_reports:bhp_utility_reports_home_url'))


bhp_utility_navbar.append_item(
    NavbarItem(name='reports',
               label='Employee Reports',
               fa_icon='fa-cogs',
               url_name='bhp_utility_reports:employees_report_listboard_url'))


bhp_utility_navbar.append_item(
    NavbarItem(name='reports',
               label='Department Timesheets',
               fa_icon='fa-cogs',
               url_name='bhp_utility_reports:departments_timesheet_report_listboard_url'))


site_navbars.register(bhp_utility_navbar)
