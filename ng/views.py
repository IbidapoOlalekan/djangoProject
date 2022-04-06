from django.http import HttpResponse
from django.shortcuts import render


def login(requests):
    return render(requests,"login.html", context={"country": "Nigerians"})


def register(requests):
    return render(requests, "register.html", context={"country": "Nigerians"})

# Create your views here.
