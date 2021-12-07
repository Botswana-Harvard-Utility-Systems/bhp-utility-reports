from edc_dashboard.listboard_filter import ListboardFilter, ListboardViewFilters


class DepartmentListboardViewFilters(ListboardViewFilters):

    all = ListboardFilter(
        name='all',
        label='All',
        lookup={})

    new = ListboardFilter(
        label='New',
        position=1,
        lookup={'status': 'new'})

    submitted = ListboardFilter(
        label='Submitted',
        position=2,
        lookup={'status': 'submitted'})

    approved = ListboardFilter(
            label='Approved',
            position=3,
            lookup={'status': 'Approved'})
    
    rejected = ListboardFilter(
        label='Rejected',
        position=4,
        lookup={'status': 'rejected'})

    varified = ListboardFilter(
        label='Varified',
        position=5,
        lookup={'status': 'varified'})

        
