from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(req):

    return render(req, "Quotations/index.html")

def new_register(req):
    valid = User.userManager.register(
        req.POST['username'],
        req.POST['email'],
        req.POST['password'],
        req.POST['confirm'],
        req.POST['birth'],
     )
    if valid[0]:
		req.session["user"] = {
			"id": valid[1].id,
			"username": valid[1].username
		}
		return redirect('/quotes')

		for error in valid[1]:
			messages.add_message(req, messages.ERROR, error)
    return redirect('/')


def new_login(req):
    valid = User.userManager.login(
        req.POST['username'],
        req.POST['password'],
    )
    if valid[0]:
        req.session["user"] = {
            "id": valid[1].id,
            "name": valid[1].username
        }
        return redirect('/quotes')
    else:
        for error in valid [1]:
            messages.add_message(req, messages.ERROR, error)
    return redirect('/')

def quotes(req):
    return render(req, "Quotations/quotes.html")
