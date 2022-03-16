FROM python:3.10.2-alpine

RUN apk add libpq-dev gcc musl-dev
RUN pip install --upgrade pip
COPY ./ ./
RUN pip install -r requirements.txt
RUN pip install gunicorn

