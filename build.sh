#!/bin/bash

echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py add_data
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD STOP"