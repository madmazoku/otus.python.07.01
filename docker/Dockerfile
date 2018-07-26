FROM python:3.6

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

COPY ./app /opt/app

RUN pip3 install -r /opt/app/requirements.txt

ENV DJANGO_ENV=dev
ENV DOCKER_CONTAINER=1

EXPOSE 8000

CMD ["uwsgi", "--ini", "/opt/app/uwsgi.ini"]