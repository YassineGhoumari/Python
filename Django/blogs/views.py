# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        "random": get_random_string(length=14),
        "whatever": "this is a string of text"
        }

    return render(request, 'blogs/index.html', context)


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, blog_id):
    print blog_id
    return HttpResponse("placeholder to display blog {}".format(blog_id))

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {}".format(blog_id))

def delete(request, blog_id):
    return redirect('/')
