from django.urls import path
from django.http import HttpResponse  # Library to return http responses
from recipes.views import home, contato, sobre


urlpatterns = [
    path("", home),
    path("contato/", contato),
    path("sobre/", sobre),
]
