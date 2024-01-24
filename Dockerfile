FROM python:slim-bullseye

## set proxy for palladium12
#ENV http_proxy "http://10.117.4.18:8080"
#ENV https_proxy "http://10.117.4.18:8080"

## install curl
RUN apt update && apt upgrade
RUN apt install curl -y

## copy script
COPY app/ app/

## Install packages
#RUN pip install flask --user
RUN pip install -r /app/requirements.txt

## Run the built product when the container launches
ENTRYPOINT python "/app/service_1.py"
