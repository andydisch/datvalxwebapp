FROM  python:3.11-alpine as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

RUN apt update && \
    apt install -y --no-install-recommends gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.11-alpine

COPY --from=builder /opt/venv /opt/venv

WORKDIR /backend

ENV PATH="/opt/venv/bin:$PATH"

COPY . .
