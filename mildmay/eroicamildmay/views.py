from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import View
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tele(request):
    context = {

    }
    return render(request, 'opening/tele-feature.html', context)

def falling(request):
    context = {

    }
    return render(request, 'opening/falling.html', context)

def col_change(request):
    context = {

    }
    return render(request, 'opening/telep.html', context)

def twhome(request):
    context = {

    }
    return render(request, 'opening/tele-skirting.html', context)

def twPast(request):
    context = {

    }
    return render(request, 'pastWork.html', context)

def twabout(request):
    context = {

    }
    return render(request, 'twwdabout.html', context)

def twcontact(request):
    context = {

    }
    return render(request, 'contact.html', context)


def twwdabout(request):

    context = {

    }

    return render(request, 'twwdabout.html', context)
