FROM node:alpine

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app

COPY --chown=node:node package*.json ./


RUN npm install -g typescript
RUN npm install -g ts-node
RUN npm install


COPY --chown=node:node ./ .
RUN chmod +x entrypoint.sh

EXPOSE 3000

CMD npx prisma db push && npm run seed && npm run dev
