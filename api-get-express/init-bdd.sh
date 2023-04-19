#!/bin/sh

# Exécution des migrations et du seed
npx prisma migrate dev --name init
npm run seed
npm run dev
