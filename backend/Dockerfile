FROM python:3.9.1-alpine

WORKDIR /app
ENV FLASK_APP app.python
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV HOST 0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]