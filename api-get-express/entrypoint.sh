#!/bin/sh

# Exécution des migrations et du seed
# npx prisma migrate dev
# npx prisma db seed --preview-feature

npm run seed
npm run dev
