# Pull pyhthon:3.7-slim-strecth container base image
FROM python:3.8.0-alpine

# Set the working directory to /flask-app
WORKDIR /flask-app

# Copy everything in the current directory to /home/flask/flask-app in the container
ADD . /flask-app

# Install the depencencies
RUN pip install --upgrade pip
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;

# sets an environment variable inside the container
ENV FLASK_APP run.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# run command to start uWSGI web server
CMD ["uwsgi", "app.ini"]