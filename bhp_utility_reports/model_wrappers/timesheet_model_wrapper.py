from edc_model_wrapper import ModelWrapper
from edc_model_wrapper.wrappers import model_relation
from django.conf import settings
from datetime import date, datetime
from timesheet.models import DailyEntry


class TimesheetModelWrapper(ModelWrapper):
    model = 'timesheet.monthlyentry'
    next_url_name = 'employee_timesheet_report_listboard_url'


    @property
    def first_name(self):
        return self.object.employee.first_name

    @property
    def last_name(self):
        return self.object.employee.last_name

    @property
    def date_submitted(self):
        return TimesheetModelWrapperHelper.date_submitted(self.object.submitted_datetime or "")

    @property
    def overtime(self):
        return TimesheetModelWrapperHelper.time_place_holder(self.object.monthly_overtime)
    
    @property
    def annual_leave_taken(self):
        return TimesheetModelWrapperHelper.time_place_holder(self.object.annual_leave_taken)

    @property
    def sick_leave_taken(self):
        return TimesheetModelWrapperHelper.time_place_holder(self.object.sick_leave_taken)

    @property
    def study_leave_taken(self):
        return TimesheetModelWrapperHelper.time_place_holder(self.object.study_leave_taken)

    @property
    def compassionate_leave_taken(self):
        return TimesheetModelWrapperHelper.time_place_holder(self.object.compassionate_leave_taken)

    @property
    def maternity_leave_taken(self):
        return TimesheetModelWrapperHelper.time_place_holder(self.object.maternity_leave_taken)

    @property
    def paternity_leave_taken(self):
        return TimesheetModelWrapperHelper.time_place_holder(self.object.paternity_leave_taken)

    @property
    def department_name(self):
        return self.object.employee.department.dept_name

    def total_hours(self):
        daily_entries = DailyEntry.objects.filter(monthly_entry_id=self.object.id)

        total_hours = 0

        for h in daily_entries:
            total_hours += h.duration
        return total_hours


class TimesheetModelWrapperHelper:
    @staticmethod
    def time_place_holder(time):
        return time if time else 0

    @staticmethod
    def date_submitted(date_time = None):
        return TimesheetModelWrapperHelper.__date_time_formatter(date_time) if date_time else "N/A"

    @staticmethod
    def date_approved(date_time):
        return TimesheetModelWrapperHelper.__date_time_formatter(date_time)

    @staticmethod
    def __date_time_formatter(date_time):
        return datetime.strftime(date_time, '%d-%m-%y %H:%M')
