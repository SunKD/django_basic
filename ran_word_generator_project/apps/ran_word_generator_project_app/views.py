# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render
from django.utils.crypto import get_random_string



# Create your views here.
def index(request):
    return render(request, 'ran_word_generator_project_app/index.html')

def generate(request):
    if 'count' in request.session:
        request.session['count'] +=1
    else:
        request.session['count'] = 0
    
    word = get_random_string(length=14)
    context={
        'word' : word
    }
    return render(request, 'ran_word_generator_project_app/index.html', context)

def reset(request):
    request.session['count']=0
    return redirect('/')
