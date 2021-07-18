FROM python:3.8-slim-buster

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /App

EXPOSE 5000
ENV PORT 5000

WORKDIR /App

CMD exec gunicorn --bind :$PORT main:app --workers 1 --threads 1 --timeout 60