from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^[/]?$', views.request_transacao, name='request_transacao'),
]