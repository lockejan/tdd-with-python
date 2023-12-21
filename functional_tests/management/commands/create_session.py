from importlib import import_module
from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model

User = get_user_model()
from django.contrib.sessions.backends.db import SessionStore
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        """configure parser to consume email field

        :parser: parser instance
        :returns: configured parser

        """
        parser.add_argument("email")

    def handle(self, **options):
        """trigger session_key creation for given email

        :**options: key_value_pairs consisting at least email as key
        :returns: writes session_key to stdout

        """
        session_key = create_pre_authenticated_session(options["email"])
        self.stdout.write(session_key)


def create_pre_authenticated_session(email):
    """create a pre authenticated session for testing purposes

    :email: string expected to be a valid e-mail
    :returns: injected session_key

    """
    user = User.objects.create(email=email)
    session = SessionStore()
    session[SESSION_KEY] = user.pk
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session.save()
    return session.session_key
