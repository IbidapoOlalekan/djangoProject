from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from ng import views
from ng.views import login, register

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register)
]
