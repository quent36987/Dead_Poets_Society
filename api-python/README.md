# API Python

The API-python is a private api, it's all the POST, PATCH and DELETE of the database. The user need to be authenticated to use it.

You can use the username: "user" with the password: "user" to connect.

url: https://dps.epita.local/private-api

## Endpoints
Endpoints are specific location where requests to update or receive information are sent.
In this api, there is multiple endpoints to post or update information about circles, writers and letters.
All the endpoints must be preceded by the api express url (https://dps.epita.local/private-api)

Method     |url                        | Json body                         | What it does

### Circles
- POST:    [/circles](https://dps.epita.local/public-api/circles); Create new circle
```json
body: {name:}
```
- POST:    [/circles/int:id/join](https://dps.epita.local/public-api/circles/int:id/join); Join circle
- PATCH    [/circles/int:id/quit](https://dps.epita.local/public-api/circles/int:id/quit); Quit circle
- /!\ DELETE endpoint not open yet

### Writers
 - POST:    [/writers](https://dps.epita.local/public-api/writers); Create a new writer
 ```json                 
 body: {title:, name:, pseudo: }
 ```
 - PATCH:   [/writers](https://dps.epita.local/public-api/writers); Update the current writer
  ```json                 
 body: {title:, pseudo: }
 ```
 - /!\ DELETE endpoint not open yet


### Letters
 - POST:    [/letters](https://dps.epita.local/public-api/letters); Post new letter              
 ```json
 body: {circleid:, subject:, content:}
 ```
 - POST:    [/letters/int:id/reply](https://dps.epita.local/public-api/letters/int:id/reply); Reply to letter
 ```json
 body: {circleid:, subject:, content:}
 ``` 
 - PATCH:   [/letters/int:id](https://dps.epita.local/public-api/letters/int:id); Update letter
 ```json
 body: {subject:, content:}             
 ```
 - DELETE:  [/letters/int:id](https://dps.epita.local/public-api/letters/int:id);                                               Delete letter with id id

 ### Tests

 To test localy, you can use you favourite browser to access https://dps.epita.local/private-api.
 You can then connect to keycloack using the username: "user" with the password: "user".
 Then by opening the console in the dev tools of your browser, you can use fetch to try different requests.

 For exemple:

```js
// Create a new circle
fetch('https://dps.epita.local/private-api/circles', {
      method: 'POST',
    body: JSON.stringify({
        name: 'Awesome Circle Name',
    }),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
}).then(res => res.json()).then(console.log)

// POST:    /letter; post a new letter
fetch('https://dps.epita.local/private-api/letter', {
      method: 'POST',
    body: JSON.stringify({
        circleid: '1',
        content: 'les poissons rouges sont bon.',
        subject: 'poissons'
    }),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
}).then(res => res.json()).then(console.log)

// POST:    /letter/int:id/reply; reply to the letter with id 1
fetch('https://dps.epita.local/private-api/letter/1/reply/', {
      method: 'POST',
    body: JSON.stringify({
        circleid: '1',
        content: 'les poissons verts sont meileurs et bio parce que verts.',
        subject: 'poissons bis'
    }),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
}).then(res => res.json()).then(console.log)
```
