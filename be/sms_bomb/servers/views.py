from django.shortcuts import render

from django.http import HttpResponse
from .models import Server


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def make_bomb(request):
    for server in Server.objects.all():
        pass #fixme