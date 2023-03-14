FROM  python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . .
