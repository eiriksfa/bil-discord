FROM python:3.8-slim

RUN apt-get update -y
RUN apt-get upgrade -y

ARG INDEX_URL

# TODO: Install requirements from pypi, package from index-url
RUN pip install discord
RUN pip install click
RUN pip install bil-discord --index-url $INDEX_URL

