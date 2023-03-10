FROM node:18.12-alpine

WORKDIR /frontend/

COPY package.json package-lock.json /frontend/

RUN npm install

COPY . /frontend/

EXPOSE 3000
