from django.contrib.auth.views import logout
from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='login_email'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
