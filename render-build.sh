#!/usr/bin/env bash
# Выполнить миграции и собрать статику
python manage.py migrate
python manage.py collectstatic --noinput