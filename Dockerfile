FROM python:3-slim-buster

RUN apt-get update -y
RUN apt-get upgrade -y

ARG INDEX_URL

RUN pip install bil-discord --index-url $INDEX_URL
