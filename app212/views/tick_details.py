from app212.auth.is_authenticated_user import IsAuthenticatedUser
from app212.models import Tick
from app212.serializers import TickResponseSerializer, TickRequestSerializer
from app212.views.responses import SuccessResponse, NotFoundResponse, BadRequestResponse, CreatedResponse
from .base_api_view import BaseApiView


class TickDetails(BaseApiView):
    permission_classes = (IsAuthenticatedUser,)

    def get(self, request, id=None):
        if not id:
            return BadRequestResponse('Tick id required')

        try:
            data = Tick.objects.get(id=id)
        except Exception as e:
            return NotFoundResponse('Tick id {} not found'.format(id))

        serializer = TickResponseSerializer(data)
        return SuccessResponse(serializer.data)

    def post(self, request):
        serializer = TickRequestSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data['user'] = request.user
            tick = Tick.objects.create(**validated_data)
            serializer = TickResponseSerializer(tick)
            return CreatedResponse(serializer.data)

        return BadRequestResponse(data=serializer.errors)
