FROM python:3.5-alpine
ADD . /code
WORKDIR /code

ENV http_proxy=http://devproxy.bloomberg.com:82
ENV https_proxy=http://devproxy.bloomberg.com:82

RUN apk update && apk add --virtual deps gcc python-dev linux-headers musl-dev postgresql-dev && apk add --no-cache libpq

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]
