# API Python

The API-python is a private api, it's all the POST, PATCH and DELETE of the database. The user need to be authenticated to use it.

url: https://dps.epita.local/private-api

## Endpoints
Endpoints are specific location where requests to update or receive information are sent.
In this api, there is multiple endpoints to post or update information about circles, writers and letters.
All the endpoints must be preceded by the api express url (https://dps.epita.local/private-api)

Method     |url                        | Json body                         | What it does

### Circles
- POST:    /circles;                   body: name;                         create new circle
- POST:    /circles/<int:id>/join;                                         join circle
- PATCH    /circles/<int:id>/quit;                                         quit circle
- /!\ DELETE endpoint not open yet

### Writers
 - POST:    /writers;                    body: title, name, pseudo;          create a new writer
 - PATCH:   /writers;                    body: title?, pseudo?;              update the current writer
 - /!\ DELETE endpoint not open yet


### Letters
 - POST:    /letters;                    body: circleid, subject, content;   post new letter
 - POST:    /letters/<int:id>/reply;     body: circleid, subject, content;   reply to letter
 - PATCH:   /letters/<int:id>;           body: subject, content;             update letter
 - DELETE:  /letters/<int:id>;                                               delete letter with id id