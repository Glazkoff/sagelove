#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0
python manage.py loaddata questions.json
uwsgi --socket=:8001 --module=backend.wsgi:application --py-autoreload=1