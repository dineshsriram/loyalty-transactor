FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install git && apt-get -y install python-pip && apt-get -y install libevent-dev python-all-dev

RUN pip install --index-url=https://pypi.python.org/simple/ --trusted-host pypi.python.org locustio gevent pyzmq

EXPOSE 8089

ADD locustfile.py /code/

CMD ["/usr/local/bin/locust", "--host", "http://web:5000", "-f", "/code/locustfile.py"]
