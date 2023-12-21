from dataclasses import asdict

from drf_standardized_errors.formatter import ExceptionFormatter
from drf_standardized_errors.types import ErrorResponse
from rest_framework import status
from rest_framework.exceptions import APIException


class ErrorMessages:
    ENTITY_NOT_FOUND = "Entity not found"
    INVALID_ENTITY = "Invalid entity `{entity}` for `{action}`"
    RESTORE_ITEMS_ERROR = "Some items could not be restored"
    INVALID_REQUEST = "Invalid request"
    INSUFFICIENT_PERMISSION = "Insufficient permissions to perform the action"
    INVALID_ACTION = "Invalid action: {action}"
    MISSING_REQUIRED_FIELDS = "Missing some mandatory fields: ({fields})"


class CustomExceptionFormatter(ExceptionFormatter):
    def format_error_response(self, error_response: ErrorResponse):
        return {"status": "error", "type": error_response.type, "errors": [asdict(o) for o in error_response.errors]}


class ErrorDetail:
    def __init__(self, detail, code):
        self.detail = detail
        self.code = code

    def __str__(self):
        return self.detail


class BaseAPIException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code
        self.detail = ErrorDetail(detail, code)


class ClientAPIExceptionHandler(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST


class ServerAPIExceptionHandler(BaseAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
