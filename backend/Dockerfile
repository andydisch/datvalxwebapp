FROM  python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /backend

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev

COPY requirements.txt /backend

RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]