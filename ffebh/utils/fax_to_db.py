import ocr, time, mysql.connector, os
from gkconverter import convert_GK_to_lat_long

def faxscan():
    text = ocr.scan()
    text = text.replace(' ','')

    strasse = text[text.find('Straße:'):text.find('Haus-Nr')]
    hausNr = text[text.find('Haus-Nr.:'):text.find('Absch')]
    ort = text[text.find('Ort:'):text.find('Koordinate:')]

    schlagwort = text[text.find('Schlagwort:'):text.find('tichwort')]

    einsatzmittel = text[text.find('EINSATZMITTEL'):text.find('BEMERKUNG')]

    lon = text[text.find('Koordinate:X:'):text.find('Y:')]
    lat = text[text.find('Y:'):text.find('-System')]

    strasse = strasse.replace('Straße:', '')
    hausNr = hausNr.replace('Haus-Nr.:', '')
    strasse = strasse + ' ' + hausNr
    ort = ort.replace('Ort:', '')
    i = 0
    while (i != 10):
        ort = ort.replace(str(i),'')
        i += 1 

    schlagwort = schlagwort.replace('Schlagwort:', '')
    schlagwort = schlagwort.replace('S', '')
    schlagwort = schlagwort.replace('s', '')

    einsatzmittel = einsatzmittel.replace('-', '')
    einsatzmittel = einsatzmittel.replace('EINSATZMITTEL', '')

    lon = lon.replace('Koordinate:X:', '')
    lat = lat.replace('Y:', '')
    coords = convert_GK_to_lat_long(int(lon), int(lat))
    lon = coords[0]
    lat = coords[1]

    print(strasse, ort, schlagwort,lon,lat)
    return strasse, ort,  schlagwort,einsatzmittel,lon,lat
def to_db(data):
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="passwort",
    database="monitor"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO einsaetze (strasse, ort, schlagwort, einsatzmittel, lon, lat) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (data[0], data[1], data[2], data[3], data[4], data[5],)
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

while True:
    if os.path.exists("/home/pi/fax/alarmfax.pdf"):
        data = faxscan()
        to_db(data)
        print('Einsatz eingetragen. Bildschirm wird umgeschalten...')
        os.system('sh /home/pi/django-test/ffebh/utils/chrome_einsatz.sh')
    else:
        print('Keine Datei')
    time.sleep(3)