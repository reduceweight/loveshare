#基础库
FROM yaochenfeng/djangobase

ENV DJANGO_APP=loveshare \
    DJANGO_VERSION=2.1.4 \
    APP_ENV=docker      \
    DJANGO_MANAGEMENT_ON_START="migrate --noinput;collectstatic --noinput"

COPY requirements.txt /usr/django/app
RUN chown -R django /usr/django/app \
    && pip install --no-cache-dir -r /usr/django/app/requirements.txt 

COPY . /usr/django/app
