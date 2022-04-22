from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):
    def authenticate(self, uid) -> (str | User | None):
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email: str) -> (str | None):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
