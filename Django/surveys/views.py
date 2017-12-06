from __future__ import unicode_literals

from django.shortcuts import render, redirect,  HttpResponse

def surveys(request):
    return render(request, 'surveys/index.html')



def process_form(request):

    print request.POST
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    request.session['tries'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['xyz']
    request.session['language'] = request.POST['xyx']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')


def display_result(request):
    return render(request, 'surveys/result.html')
