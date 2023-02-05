# Django views are Python functions that takes http requests and returns http response.
# You will add it on your Python path.
from django.shortcuts import render
import requests


def home(request):
    return render (request, 'home.html' )


