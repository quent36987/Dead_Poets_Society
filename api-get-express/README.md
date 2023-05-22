# API Express

The API Express is a public api, it's all the GET to the database. The user don't need to be authenticated to use it.

url: https://dps.epita.local/public-api

## Endpoints
Endpoints are specific location where requests for information are sent. They are used to get information or resources.
In this api, there is multiple endpoints to get information about circles, writers and letters.
All the endpoints must be preceded by the api express url (https://dps.epita.local/public-api)

### Circles
/circles : get all the circles
/circles/{id} : get information about the specified circle
/circles/{id}/writers : get writers belonging to the circle
/circles/{id}/letters :

{id} must be replaced with a circle id

### Writers
/writers : get all the writers
/writers/{id} : get information about the specified writer
/writers/{id}/letters : get letters written by the writer
/writers/{id}/circles : get membership circles of the writer
/writers/{id}/circles/{circleId}/letters : get letters from the specified writer into the specified circle

{id} must be replaced with a writer id
{circleId} must be replaced with a circle id

### Letters
/letters : get all the letters
/letters/{id} : get information about the specified letter
/letters/{id}/writers :
/letters/{id}/circles :

{id} must be replaced with a letter id