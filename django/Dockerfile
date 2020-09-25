FROM ubuntu:18.04

RUN apt-get -y update \
  && apt-get install -y locales python3-pip python3.7 libmysqlclient-dev\
  && mkdir /src \
  && rm -rf /var/lib/apt/lists/* \
  && echo "ja_JP UTF-8" > /etc/locale.gen \
  && locale-gen
RUN apt-get update && \
    apt-get install nginx -y 

WORKDIR /src
ADD ./ /src/
RUN LC_ALL=ja_JP.UTF-8 pip3 install -r requirements.txt

ENTRYPOINT ["nginx", "-g", "daemon off;"]
