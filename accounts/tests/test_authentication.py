from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend
from accounts.models import Token

EXAMPLE_MAIL = 'edith@example.com'

User = get_user_model()


class AuthenticateTest(TestCase):
    def test_returns_None_if_no_such_token(self):
        result = PasswordlessAuthenticationBackend().authenticate(
            'c26b1778-1b23-4b7c-b984-29cdf40e5500')
        self.assertIsNone(result)

    def test_returns_new_user_with_correct_email_if_token_exists(self):
        token = Token.objects.create(email=EXAMPLE_MAIL)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        new_user = User.objects.get(email=EXAMPLE_MAIL)
        self.assertEqual(user, new_user)

    def test_returns_existing_user_with_correct_email_if_token_exists(self):
        existing_user = User.objects.create(email=EXAMPLE_MAIL)
        token = Token.objects.create(email=EXAMPLE_MAIL)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        self.assertEqual(user, existing_user)


class GetUserTest(TestCase):
    def test_gets_user_by_email(self):
        User.objects.create(email='another@example.com')
        desired_user = User.objects.create(email=EXAMPLE_MAIL)
        found_user = PasswordlessAuthenticationBackend().get_user(
            EXAMPLE_MAIL)
        self.assertEqual(found_user, desired_user)

    def test_returns_None_if_no_user_with_that_email(self):
        self.assertIsNone(
            PasswordlessAuthenticationBackend().get_user(EXAMPLE_MAIL))
