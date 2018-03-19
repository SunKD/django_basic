# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import time
import random

# Create your views here.
def index(request):
    if 'golds' not in request.session:
        request.session['golds'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'ninja_gold_project_app/index.html')


def process(request):
    activity = request.session['activity']
    location = request.POST['location']
    if location == "farm":
        money = random.randrange(10, 21)
    elif location == "cave":
        money = random.randrange(5, 11)
    elif location == "house":
        money = random.randrange(2, 6)
    elif location == "casino":
        money = random.randrange(-50, 51)

    if money < 0:
        activity.append("<p class='red'>Entered Casino and lost " + str(money) + " golds... Ouch. (" + str(time.strftime("%Y-%m-%d %H:%M")) + " )</p>")
    else:
        activity.append("<p class='green'>Earns " + str(money) + " golds from the " + location + " (" + str(time.strftime("%Y-%m-%d %H:%M")) + " )</p>")  
    
    request.session['golds'] += money
    request.session['activity'] = activity
    print location
    print request.session['activity']
    return redirect('/')
