from rest_framework import pagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "response": {
                    "data": data,
                    "pagination": {
                        "next": self.get_next_link(),
                        "previous": self.get_previous_link(),
                        "count": self.count,
                    },
                },
                "status": "success",
                "message": None,
            }
        )
