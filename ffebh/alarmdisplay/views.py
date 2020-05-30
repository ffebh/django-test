from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import Http404
from django.template import Context, loader

# Create your views here.

def HomePageView(request):
    t = loader.get_template('home.html')
    return HttpResponse(t.render({"inhalt":"Hier könnte Ihre Werbung stehen"}))

class UhrView(TemplateView):
    template_name = 'uhr.html'


