FROM python:3.8-alpine

ADD ./ffebh/ /opt/ffebh
ADD requirements.txt /opt/ffebh/requirements.txt

RUN pip install -r /opt/ffebh/requirements.txt && \
  python /opt/ffebh/manage.py makemigrations && \
  python /opt/ffebh/manage.py migrate

EXPOSE 8000/tcp

CMD ["python", "/opt/ffebh/manage.py", "runserver", "0.0.0.0:8000"]