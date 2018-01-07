FROM python:3.5-alpine
ADD . /code
WORKDIR /code

RUN apk update && apk add --virtual deps gcc python-dev linux-headers musl-dev postgresql-dev && apk add --no-cache libpq

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]
