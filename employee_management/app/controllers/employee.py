from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from employee_management.app.models.employee import Employee
from employee_management.app.serializers.employee import EmployeeSerializer
from employee_management.app.utils.pagination import CustomLimitOffsetPagination
from employee_management.app.utils.responses import StandardResponse


class EmployeeListCreateAPIView(APIView, CustomLimitOffsetPagination):
    def get(self, request):
        employees_qs = Employee.objects.all()
        page = self.paginate_queryset(employees_qs, request, view=self)
        if page is not None:
            serializer = EmployeeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # Return all the items
        serializer = EmployeeSerializer(employees_qs, many=True)
        return StandardResponse(serializer.data)

    @staticmethod
    def post(request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return StandardResponse(serializer.data, status=status.HTTP_201_CREATED)
        return ValidationError(serializer.errors)


class EmployeeRetrieveUpdateDeleteAPIView(APIView):
    @staticmethod
    def get(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return StandardResponse(serializer.data)

    @staticmethod
    def put(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return StandardResponse(serializer.data)
        return ValidationError(serializer.errors)

    @staticmethod
    def delete(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return StandardResponse(status=status.HTTP_204_NO_CONTENT)
