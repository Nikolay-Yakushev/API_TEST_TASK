FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3.8 python3-pip
RUN apt install vim -y
COPY django_poll_api /home/django_poll_api
WORKDIR /home/django_poll_api
RUN pip3 install -r requirements.tx
