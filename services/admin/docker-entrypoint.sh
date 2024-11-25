#!/bin/bash


python manage.py check --deploy

python manage.py migrate --no-input

python manage.py createsuperuser --no-input \
    --username $ADMIN_DJANGO_SUPERUSER_USERNAME \
    --email $ADMIN_DJANGO_SUPERUSER_EMAIL \
    --password $ADMIN_DJANGO_SUPERUSER_PASSWORD

python manage.py collectstatic --no-input

uwsgi --strict --ini uwsgi.ini