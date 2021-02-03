FROM python:3.9.1-buster


WORKDIR /app
COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY . .
ENV FLASK_APP app.py
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]