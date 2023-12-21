from django.contrib import admin

from employee_management.app.models.employee import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
