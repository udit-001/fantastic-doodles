#!/bin/bash

python manage.py migrate
python manage.py collectstatic
gunicorn --bind 0.0.0.0:8000 --log-level INFO youtube_search.wsgi:application