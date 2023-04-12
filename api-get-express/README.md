# SOA Project TP1

> Adrien LORGE
> Annabelle CHEVREAU
> Florian REIMAT
> Quentin GOUJON

## How to install / launch it

```sh
git clone https://gitlab.cri.epita.fr/florian.reimat/soa_rest.git

# If you are on Nix
# nix-shell

cp .env.default .env

docker-compose up -d

npx prisma migrate dev --name init

npm run seed
npm run dev
```

Please don't forget to setup the env file before launching the docker-compose
The default .env file is this one [.env.default](.env.default).
