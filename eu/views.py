from django.http import HttpResponse
from django.shortcuts import render


def eu_login(requests):
    return render(requests, "login.html", context={"country": "Europeans"})


def eu_register(requests):
    return render(requests, "register.html", context={"country": "Europeans"})

# Create your views here.
