FROM ubuntu:latest
LABEL "author"="kutbuddin"
LABEL "project"="tooplate"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install git -y
RUN apt update && apt install apache2 -y 
EXPOSE 80
WORKDIR /var/www/html
VOLUME /var/log/apache2
ADD nano.tar.tz  /var/www/html