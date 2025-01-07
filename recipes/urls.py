from django.urls import path
from django.http import HttpResponse  # Library to return http responses
from recipes.views import home


urlpatterns = [
    path("", home),
]
