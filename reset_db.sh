#!/bin/bash

rm db.sqlite3
sleep 1
python manage.py migrate
sleep 1
python manage.py loaddata pushers/fixtures/*.json