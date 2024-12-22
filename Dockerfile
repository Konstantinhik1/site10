FROM python:3.12

WORKDIR /app

COPY requirments.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y bash

COPY mysite .
