from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from app212.models import Token


class App212TokenAuthenticator(TokenAuthentication):
    model = Token

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        if token.user.is_deleted:
            raise AuthenticationFailed("User is deleted")

        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        token.update_last_used()
        token.update_times_used()
        token.save()

        return token.user, token
