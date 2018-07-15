FROM  node:alpine as NODE
WORKDIR /usr/src/app
COPY frontend .
RUN npm install && npm run build


FROM docker pull yaochenfeng/djangobase

ENV PYTHONUNBUFFERED 1
ENV DJANGO_APP=loveshare \
    DJANGO_VERSION=2.0.7 \
    PYTZ_VERSION=2018.5 \
    APP_ENV=docker      \
    DJANGO_MANAGEMENT_ON_START="migrate --noinput;collectstatic --noinput"


COPY requirements.txt /usr/django/app
RUN pip install --no-cache-dir -r /usr/django/app/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY . /usr/django/app
COPY --from=NODE /usr/src/app/dist/ /usr/django/app/frontend/dist/
