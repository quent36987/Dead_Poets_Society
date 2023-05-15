# DEAD POETS SOCIETY

This project is an example of diverse services, who works together to provide a fake social network.
the authentication is done with OpenID Connect with keycloak.
the redirection is done with apache2.
the bbd is done with postgresql.
the backend is done with 2 api, one public (express + typescript) and one private (python + flask).
the frontend is done with react.
an example of pub/sub is done with redis and python.

## Installation

clone the project
```
cd DeadPoetsSociety
cp .env.dev .env
```
install docker
```
docker-compose build && docker compose up -d
```
add "127.0.0.1 dps.epita.local" to your /etc/hosts

enjoy and try !

## SERVICES

### Keycloak

keycloak is an open source identity and access management solution. It makes it easy to secure applications and services with little to no code.

admin console : https://dps.epita.local/auth/admin

user: admin & password: admin

logout: https://dps.epita.local/redirect_oidc?logout=get

### Postgresql

PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
We use it to store all the data of the social network.

It's run on port 5432 in the docker-compose.yml

The default user is postgres and the password is postgres

### Redis

Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.
We use it to store the messages of the pub/sub system.

it's run on port 6379 in the docker-compose.yml


### Apache

Apache is a free and open-source cross-platform web server software.
We use it to redirect the user to the right service. (frontend, backend, keycloak, etc..)

The domain https://dps.epita.local is redirect to the apache server.

The apache server manage the authentication with keycloak, and redirect the user to keycloak if he is not authenticated.

### Frontend

The frontend is a react app, who use the public api to get the data. 
It's nothing yet. It's juste here to show how to add a frontend to the project.

url : https://dps.epita.local/front

### API Python

The API Python is a private api, it's all the PUT, POST, DELETE, PATCH to the database.
The user need to be authenticated to use it.

url : https://dps.epita.local/private-api/

### API Express

The API Express is a public api, it's all the GET to the database.
The user don't need to be authenticated to use it.

url : https://dps.epita.local/public-api/

