FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV APP_DIR /usr/src/app

RUN mkdir ${APP_DIR}
WORKDIR ${APP_DIR}
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
