# API Express

The API Express is a public api, it's all the GET to the database. The user don't need to be authenticated to use it.

url: https://dps.epita.local/public-api

## Endpoints
Endpoints are specific location where requests for information are sent. They are used to get information or resources. <br />
In this api, there is multiple endpoints to get information about circles, writers and letters. <br />
All the endpoints must be preceded by the api express url (https://dps.epita.local/public-api)

### Circles
[/circles](https://dps.epita.local/public-api/circles) : get all the circles <br />
[/circles/{circleId}](https://dps.epita.local/public-api/circles/1) : get information about the specified circle <br />
[/circles/{circleId}/writers](https://dps.epita.local/public-api/circles/1/writers) : get writers belonging to the circle <br />
[/circles/{circleId}/letters](https://dps.epita.local/public-api/circles/1/letters) : get letters from the specified circle

{circleId} must be replaced with a circle id

### Writers
[/writers](https://dps.epita.local/public-api/writers) : get all the writers <br />
[/writers/{writerId}](https://dps.epita.local/public-api/writers/1) : get information about the specified writer <br />
[/writers/{writerId}/letters](https://dps.epita.local/public-api/writers/1/letters) : get letters written by the writer <br />
[/writers/{writerId}/circles](https://dps.epita.local/public-api/writers/1/circles) : get membership circles of the writer <br />
[/writers/{writerId}/circles/{circleId}/letters](https://dps.epita.local/public-api/writers/1/circles/1/letters) : get letters from the specified writer into the specified circle

{writerId} must be replaced with a writer id <br />
{circleId} must be replaced with a circle id

### Letters
[/letters](https://dps.epita.local/public-api/letters) : get all the letters <br />
[/letters/{letterId}](https://dps.epita.local/public-api/letters/1) : get information about the specified letter <br />
[/letters/{letterId}/writer](https://dps.epita.local/public-api/letters/1/writer) : get the letter writer <br />
[/letters/{letterId}/circle](https://dps.epita.local/public-api/letters/1/circle) : get membership circles of the letter

{letterId} must be replaced with a letter id