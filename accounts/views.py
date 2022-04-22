from django.contrib import auth, messages
from django.core.mail import send_mail
from django.http.request import HttpRequest
from django.shortcuts import redirect
from django.urls.base import reverse

from accounts.models import Token


def send_login_email(
    request: HttpRequest
) -> (HttpResponsePermanentRedirect | HttpResponseRedirect):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid))
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@smittie.de',
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in.")
    return redirect('/')


def login(
    request: HttpRequest
) -> (HttpResponsePermanentRedirect | HttpResponseRedirect):
    # token = request.GET.get('token')
    # print(token)
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
