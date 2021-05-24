from rest_framework import status
from rest_framework.views import Response


class NotFoundResponse(Response):

    def __init__(self, message=None, data=None):
        super().__init__(data=data or {'detail': str(message)}, status=status.HTTP_404_NOT_FOUND)
