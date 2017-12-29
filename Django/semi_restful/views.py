# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from .models import User

# Create your views here.

def index(request):
    print "Inside the index method."

    context = {
        'users': User.objects.all()

    }

    return render(request, 'semi_restful/index.html', context)

def new(request):
    print "Inside the new method."

    return render(request, 'semi_restful/new.html')

def create(request):
    if request.method == "POST":
        pass
        #validate
        errors = User.objects.validate(request.POST)

        #if erros exist
        if errors:
            pass # flash errors


        # create the users
        user = User.objects.create_user(request.POST)

        # redirect user's sho page
        return redirect( reverse('show_user', kwargs = {'id': user.id}))

    return redirect(reverse('new_user'))

def show(request, id):
    user = User.objects.get(id = id)

    context = {
        'user' : user,
    }

    return render(request, 'semi_restful/show.html', context)
