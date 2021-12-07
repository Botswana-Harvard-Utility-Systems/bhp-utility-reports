from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters


class EmployeeListboardViewFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        label='All',
        lookup={})

    department = ListboardFilter(
        label='Department',
        position=10,
        lookup={'department': True})
