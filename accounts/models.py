import uuid
from django.db import models


class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True


class Token(models.Model):
    uid = models.UUIDField(primary_key=True,
                           default=uuid.uuid4,
                           editable=False,
                           max_length=40)
    email = models.EmailField()
