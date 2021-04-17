# SecZetta Integrations 

## Purpose

The purpose of this repository is to fully document what it takes to integrate with SecZetta's partner network.

Some of the integrations will be build inside of SecZetta. Some will require external scripts to be accomplished. The documentation and subsequent configuration files stored here will be used by our customers and partners to deploy these integrations within the *SecZetta Identity Suite*. 

## Getting Started

In order to build out any type of integration listed herein, how the various tools commuicate will be a top priority. In most, SecZetta will use one of three ways to communiate:

* External Party uses SecZetta's API endpoint: `<seczetta-tenant-name>.mynonemployee.com/api/<endpoint>`
  * Click [here](https://seczetta.nonemployee.com/api/v1) for API Documentation
  * Also, documentation related to your tenant can be found at `<seczetta-tenant-name>.mynonemployee.com/api/v1`
* SecZetta uses REST API Action within its own workflows
* An external script runs in the customer's network to pull and push data to and from SecZetta

## Using SecZetta's API

In order to start using SecZetta's API, an API key will need to be created. SecZetta currently uses Token based AuthN to secure the API endpoint.

### Generate API Key

In order to generate an API Key follow these steps: 

1. Navigate to the [admin](#seczetta-admin-dashboard) side of SecZetta (NEProfile dashboard). 

2. Click into [`System -> api`](#seczetta-api-page)

3. Click the `+ Api Key` button and copy your API Key

#### SecZetta Admin Dashboard

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/seczetta-dashboard-admin-button.png" width="50%"/>

#### SecZetta API Page

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/seczetta-api-keys.png" width="50%"/>

### Authentication

SecZetta can use API keys to allow full access to the API. SecZetta supports basic authentication for it's API; however, it is recommended to use Token-based auth.

If using token auth, SecZetta expects for the token to be included in all API Requests to the server in a header that looks like the following:

* `Authorization: Token token=YOUR_API_TOKEN_HERE`

> You must replace YOUR_API_TOKEN_HERE with your personal API key.

### Sending your first request

The easiest way to test that you can call the SecZetta API correctly is to do a `GET` request on the `/users` endpoint. The only other requirement to send out the request is to add one more header to the request:

* `Accept: */*`

Using a tool like [Postman](getpostman.com), do your initial test using the `GET /users` endpoint. See the below example for details. Remember to replace the example values with values the represent your SecZetta instance

#### Example Request:

Field         | Value
--------------|-
HTTP VERB     | `GET`
HTTP URL      | `https://acme.mynonemployee.com/api/users`
HTTP Header 1 | `Authorization: Token token=c7aef210f92142188032f5a7b59ed0f6`
HTTP Header 2 | `Accept: */*`

#### Example Response:

```jsonc
200 OK

{
    "users": [
        {
            "id": "f5d149f0-44b9-4bde-9d68-16c0598811bb",
            "uid": "a25e6cd522264643bd3d49fc69c7d0ec",
            "type": "NeprofileUser",
            "name": "System User",
            "email": "system@neprofile.com",
            "title": "system User",
            "status": "Active",
            "login": "NeProfile0",
            "last_login": "2021-04-05T13:30:22.000-04:00",
            "cookies_accepted_at": null
        },
        // ... more users
    ]
}
```