from rest_framework import status
from rest_framework.views import Response


class CreatedResponse(Response):

    def __init__(self, data=None):
        super().__init__(data=data, status=status.HTTP_201_CREATED)
