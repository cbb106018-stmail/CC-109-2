FROM python:3.7
MAINTAINER CBB106018

ADD . /websites
WORKDIR /websites

RUN pip3 install --upgrade pip
RUN pip3 install -r requirement.txt

CMD ["uwsgi", "app.ini"]
