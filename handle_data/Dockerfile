FROM python:3.7
MAINTAINER CBB106018

ADD . /handle_data
WORKDIR /handle_data

RUN pip3 install --upgrade pip
RUN pip3 install -r requirement.txt

CMD ["python3", "handler.py"]
