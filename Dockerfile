FROM python:3.8-alpine as base

FROM base as builder

RUN mkdir -p /home

WORKDIR /home

COPY . /home
RUN ls -la /

CMD ["python3", "./dock.py"]