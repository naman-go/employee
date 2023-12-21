from rest_framework import serializers

from employee_management.app.models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ["created_on", "created_by", "updated_on", "updated_by", "deleted_on", "deleted_by", "is_deleted"]
