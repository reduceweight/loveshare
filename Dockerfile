FROM  node:alpine as NODE
WORKDIR /usr/src/app
COPY frontend .
RUN npm install && npm run build


FROM yaochenfeng/djangobase

ENV DJANGO_APP=loveshare \
    DJANGO_VERSION=2.0.7 \
    APP_ENV=docker      \
    DJANGO_MANAGEMENT_ON_START="migrate --noinput;collectstatic --noinput"

COPY requirements.txt /usr/django/app
RUN chown -R django /usr/django/app \
    && pip install --no-cache-dir -r /usr/django/app/requirements.txt 

COPY . /usr/django/app
COPY --from=NODE /usr/src/app/dist/ /usr/django/app/frontend/dist/
