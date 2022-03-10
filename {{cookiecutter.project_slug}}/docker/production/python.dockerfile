#########################
# PRODUCTION DOCKERFILE #
#########################
FROM python:3.9-alpine

LABEL maintainer="{{ cookiecutter.author_name }}"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
