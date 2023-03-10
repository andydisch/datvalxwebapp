FROM node:18.12-alpine

WORKDIR /app/frontend/

COPY package.json package-lock.json /app/frontend/

RUN npm install

COPY . /app/frontend/

EXPOSE 3000

CMD ["npm", "start"]