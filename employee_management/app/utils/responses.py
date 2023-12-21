from rest_framework import status
from rest_framework.response import Response


class StandardResponseMessages:
    status_mapping = {
        200: "Request was successful",
        201: "Resource created successfully",
        204: "Resource deleted successfully",
        400: "Bad request",
        404: "Resource not found",
        500: "Internal server error",
    }


class StandardResponse(Response):
    def __init__(self, data=None, status=status.HTTP_200_OK, message=None, **kwargs):
        formatted_data = {
            "response": {
                "data": data,
            },
            "status": "success" if status < 400 else "error",
            "message": message or StandardResponseMessages.status_mapping.get(status, None),
        }
        super().__init__(data=formatted_data, status=status, **kwargs)
