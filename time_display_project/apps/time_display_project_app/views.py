# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

# Create your views here.
def index(request):
    context = {
        "date": strftime("%Y-%m-%d", localtime()),
        "time": strftime("%H:%M %p", localtime())
    }
    return render(request, 'time_display_project_app/index.html', context)
