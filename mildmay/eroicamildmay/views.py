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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



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

@csrf_exempt
def justsentemail(request):

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

    MY_ADDRESS = 'eroicamildmay@outlook.com';
    ER_INFO = 'twoodhouse97@gmail.com';
    ER_INF = 'eroicamildmay@outlook.com'
    PASSWORD = 'wun-7hm-LXT-z25';
    PASSWORDN = 'Vta-bkD-YGH-Ri9';

    try:


        eroica_server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        eroica_server.starttls();
        eroica_server.login(MY_ADDRESS, PASSWORDN);
    except:
        print('error E1');




    if request.method == 'POST':

        origin_name = request.POST['namm']
        origin_email = request.POST['emm']
        message_body = request.POST['mess']



        Message.objects.create(
        name = origin_name,
        email = origin_email,
        message = message_body
        )

        try:

            msg = MIMEMultipart()       # create a message

            # setup the parameters of the message
            msg['From']=MY_ADDRESS
            msg['To']=ER_INF
            msg['Subject']="Message From "+origin_name;
            mess_header = 'Message From: '+origin_name+' \n\nContact details: '+origin_email+'\n\nMessage: \n\n';
            message = mess_header + message_body;

            msg.attach(MIMEText(message, 'plain'))
            print(3);
            # send the message via the server set up earlier.
            eroica_server.send_message(msg)
            print(4);
            del msg

            print('SENT THE MAIL.')
        except:
            print('error E2');

        return HttpResponse(status=200)


def twwdabout(request):

    context = {

    }

    return render(request, 'twwdabout.html', context)
