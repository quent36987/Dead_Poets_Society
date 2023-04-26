# DEAD POETS SOCIETY

This project is an example of diverse services, who works together to provide a fake social network.
the authentication is done with OpenID Connect with keycloak.
the redirection is done with apache2.
the bbd is done with postgresql.
the backend is done with 2 api, one public (express + typescript) and one private (python + flask).
the frontend is done with react.
an example of pub/sub is done with redis and python.

## Installation

- clone the project
- cd DeadPoetsSociety
- cp .env.dev .env
- install docker and docker-compose build && docker compose up -d
- enjoy and try !


domain : https://dps.epita.local

https://dps.epita.local/public-api/

https://dps.epita.local/private-api/

https://dps.epita.local/redirect_oidc?logout=get
