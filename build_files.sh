#!/bin/bash
pip install -r requirements.txt
python3.x manage.py collectstatic --noinput
