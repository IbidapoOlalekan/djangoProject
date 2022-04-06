from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from eu.views import eu_login, eu_register

urlpatterns = [

    path('login/', eu_login),
    path('register/', eu_register),
]
