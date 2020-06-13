import pytesseract
from PIL import Image
import os
import time
def scan():
    os.system('gs -o /home/max/django-test/ffebh/utils/fax.jpg -r500 -sDEVICE=jpeg /home/max/django-test/ffebh/utils/testfax.pdf')
    text = pytesseract.image_to_string(Image.open('/home/max/django-test/ffebh/utils/fax.jpg'), lang='deu')
    return text

