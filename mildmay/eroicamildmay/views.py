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
from .models import Message
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from .eroica_mail import Eroica_SMTP;



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
    return render(request, 'opening/new-feature.html', context)

def land(request):
    context = {

    }
    return render(request, 'opening/land.html', context)


def oldhome(request):
    context = {

    }
    return render(request, 'opening_old/telep.html', context)

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

@csrf_exempt
def cont(request):
    if request.method == 'POST':
        namm = request.POST['namm']
        emm = request.POST['emm']
        mess = request.POST['mess']
        print(namm)
        print(emm)
        print(mess)

        try:
            email_help = Eroica_SMTP();
            email_help.send_mail(namm,emm,mess);
        except:
            print('error E3');


        Message.objects.create(
        name = namm,
        email = emm,
        message = mess
        )

        return HttpResponse(status=200)


def twwdabout(request):

    context = {

    }

    return render(request, 'twwdabout.html', context)
