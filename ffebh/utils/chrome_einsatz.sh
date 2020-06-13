pkill chrome-browse
chrome-browser --start-fullscreen 192.168.188.81:8000/einsatz
ssh -t 192.168.0.15 'pkill chrome-browse'
ssh -t 192.168.0.15 'DISPLAY=:0 chrome-browser --start-fullscreen 192.168.188.81:8000/einsatz'
rm /home/max/django-test/ffebh/utils/fax.jpg