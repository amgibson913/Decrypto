#!/bin/bash
source venv/bin/activate
exec gunicorn --worker-class eventlet -w 1 -b :5000 --access-logfile - --error-logfile - app:app