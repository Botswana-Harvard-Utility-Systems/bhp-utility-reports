from edc_model_wrapper import ModelWrapper
from edc_model_wrapper.wrappers import model_relation
from django.conf import settings


class EmployeeModelWrapper(ModelWrapper):
    model = 'bhp_personnel.employee'
    next_url_name = 'employees_report_listboard_url'

    @property
    def department(self):
        return self.object.department.dept_name

    @property
    def supervisor(self):
        return f'{self.object.supervisor.first_name} {self.object.supervisor.last_name}'
