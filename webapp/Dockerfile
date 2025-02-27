FROM python:3.13.2-slim-bookworm

USER root
WORKDIR /root/.pip

COPY pip.conf ./pip.conf

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt
