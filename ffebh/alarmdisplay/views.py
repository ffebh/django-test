from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import Context, loader
from django.conf import settings
import os
from utils import now
# Create your views here.

def HomePageView(request):
    t = loader.get_template('home.html')
    #read txt file in static folder
    file = open(os.path.join(settings.STATICFILES_DIRS[0], 'test.txt'),mode='r')
    inhalt = file.read()
    file.close()

    return HttpResponse(t.render({"inhalt": inhalt}))

class UhrView(TemplateView):
    template_name = 'uhr.html'

def EinsatzView(request):
    t = loader.get_template('einsatz.html')
    #Demonstration zum Aufruf externer Python Skripte. Diese müssen vorher importiert werden siehe oben
    i = now.now()
    return HttpResponse(t.render({'inhalt':i}))


