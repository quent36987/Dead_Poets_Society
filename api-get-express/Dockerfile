FROM node:alpine

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app

COPY --chown=node:node package*.json ./


RUN npm install -g typescript
RUN npm install -g ts-node
USER node
RUN npm install


COPY --chown=node:node ./ .

EXPOSE 3000

CMD npx prisma migrate dev --name init && npm run seed && npm run dev
