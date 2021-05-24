from rest_framework import status
from rest_framework.views import Response


class SuccessResponse(Response):

    def __init__(self, data=None):
        super().__init__(data=data, status=status.HTTP_200_OK)
