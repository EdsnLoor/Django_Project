from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import models


# Create your views here.
def index(request):
    return HttpResponse('HELLO')
