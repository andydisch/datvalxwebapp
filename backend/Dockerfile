FROM  python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /backend

COPY requirements.txt /backend

RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 8000
