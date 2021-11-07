FROM node:12.9.0-alpine
USER node
WORKDIR /home/node/app/

COPY public public
COPY package.json .
COPY server.js .
COPY package.json .

RUN npm install
CMD ["npm", "run", "is"]
