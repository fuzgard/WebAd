#!/usr/bin/env bash
# Выполнить миграции и собрать статику
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput