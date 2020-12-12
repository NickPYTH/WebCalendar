from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404


def main_page(request):
    return render(request, "index.html")