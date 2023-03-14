FROM  python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r /requirements.txt
COPY . .
