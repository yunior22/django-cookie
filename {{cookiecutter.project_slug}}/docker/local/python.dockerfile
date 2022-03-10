##########################
# DEVELOPMENT DOCKERFILE #
##########################
FROM python:3.9-alpine

LABEL maintainer="{{ cookiecutter.author_name }}"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/web
WORKDIR /usr/src/web

COPY requirements/local.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D django
RUN chown -R django:django /vol/
RUN chmod -R 755 /vol/web
USER django
