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
    
    #import mysql.connector
    #mydb = mysql.connector.connect(
    #host="localhost",
    # user="user",
    # passwd="password"
    # )
    # mycursor = mydb.cursor()

    # mycursor.execute("select * from alarmdisplay.einsaetze order by id desc limit 1")

    # db = mycursor.fetchall()

    # for row in db:
    #     id = row[0]
    #     strasse = row[1]
    #     ort = row[2]
    #     schlagwort = row[3]
    #     alarmzeit = row[4]
    #     einsatzmittel = row[5]
    #     lon = row[6]
    #     lat = row[7]

    id = 1
    strasse = 'Musterstraße 1'
    ort = 'Musterort'
    schlagwort = 'Musterschlagwort'
    alarmzeit = 'Musterzeit'
    einsatzmittel = 'Mustereinsatzmittel'
    lon = 'Musterlängengrad'
    lat = 'Musterbreitengrad'
    #Demonstration zum Aufruf externer Python Skripte. Diese müssen vorher importiert werden siehe oben
    #i = ocr.scan()
    data = {'id':id, 'strasse':strasse, 'ort':ort, 'schlagwort':schlagwort, 'alarmzeit':alarmzeit, 'einsatzmittel':einsatzmittel, 'lon':lon, 'lat':lat}
    return HttpResponse(t.render(data))


