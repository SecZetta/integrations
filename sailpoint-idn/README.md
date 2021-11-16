# SecZetta / SailPoint IDN Integration

## Contents

- [SecZetta / SailPoint IDN Integration](#seczetta---bitsight-integration)
  - [Overview](#overview)
    - [Architecture Overview](#architecture-overview)
  - [Supported Features](#supported-features)
  - [Prerequisites](#prerequisites)
    - [Generating a SecZetta API Key](#generating-a-seczetta-api-key)
      - [SecZetta Admin Dashboard](#seczetta-admin-dashboard)
      - [SecZetta API Page](#seczetta-api-page)
    - [Getting BitSight API Token](#getting-bitsight-api-token)
      - [Account Dropdown](#account-dropdown)
      - [Generate BitSight API Key](#generate-bitsight-api-key)
  - [Configuration](#configuration)
    - [Integration Script](#integration-script)
  - [API Usage](#api-usage)
    - [BitSight API](#bitsight-api)
      - [Authentication](#authentication)
      - [GET /ratings/v1/companies](#get--ratings-v1-companies)

## Overview

The main purpose of the SecZetta / SailPoint integration is to be able to pass profile data back and forth between systems. Please see a more generic IAM overview [here](https://github.com/SecZetta/integrations/tree/main/iam). 

## Supported Features

The SecZetta / IdentityNow (IDN) integration can be configured in a few different ways. Depending on the configuration some features may not be fully supported:

- Profile Management
  - Data aggregation (SailPoint IDN Initiated)
    - Utilizing the SailPoint WebServices connector
    - Read in SecZetta Profiles
    - API Integration (SecZetta Initiated)
      - Utliizing SecZetta’s REST API Workflow action
      - Create, Update, Delete Identity cubes

## Prerequisites
- Data Aggregation:
  - Administrative access in SecZetta and IDN
  - A SecZetta API token ( Admin  system  api)
  - The Profile Type ID for the profiles that are be- g aggregated
- API Integration
  - Administrative Access in SecZetta and IDN
  - IDN OAuth 2.0 Client with client_id and client_secret

## High Level Architecture

### Data Aggregation

![SZ Initiated](img/sailpoint-idn-sz-initiated-arch.png)

### API Integration

![IDN Initiated](img/sailpoint-idn-iam-initiated-arch.png)

## Configuration Parameters

This section provides the required configuration for the features described above:

### Data Aggregation (IDN Initiated)
The Data aggregation integration requires an IDN Web Services connector. This connector will utilize the /profiles endpoint of the SecZetta API

#### SailPoint Connector Configuration
Create a new source connector and then refer to the following table for the parameters required to setup the connector:

Parameter | Description
--------- | --------------
Source Name | SecZetta
Source Description | SecZetta connector
Authentication Settings | No / Custom Authentication
Base URL | `https://<your-seczetta-tenant-url>/api` <br/>
(i.e. https://company.mynonemployee.com)
HTTP Operations (HO) | Add 1 operation (could also add a test connection operations if you choose)
General Information -> Operation Name | Aggregate Users
General Information -> Operation Type | Account Aggregation
General Information -> Context Url | `/profiles?profile_type_id=<profile_type_id>&query[limit]=<limit>&query[offset]=0`  </br> </br> *Notice there are 2 ‘variables’ there profile_type_id and limit* </br></br> The profile_type_id variable is specific to your environment. More details below on how to grab your profile_type_id. Normally you would want the people profile type </br></br>The limit variable is used to return a set number of profiles per API call (this api endpoint uses paging, see below for more details)
General Information -> HTTP Method | GET
Header -> Key/Value |Add 3 key/value pairs under the header tab: </br> Authorization: Token token=<your-seczetta-token> </br> Accept: application/json </br> Content-Type: application/json
Body |No Body required
Response Information -> Root Path | Profiles
Response Information -> Success Code | 200
Response Mapping | Here is where you map the response of the SecZetta API to IdentityNow. Remember to use attributes.<attribute-name>
Paging -> Initial Page Offset | 0
Paging -> Paging Steps | $sz_limit$ = 100 </br>TERMINATE_IF $RECORDS_COUNT$ < $sz_limit$</br>$sz_offset$ = $sz_offset$ + $sz_limit$</br>$endpoint.fullUrl$ = $application.baseUrl$ + "/profiles?profile_type_id=<profile_type_id> &query[limit]=" + $sz_limit$ + "&query[offset]=" + $sz_offset$</br></br>*More details below*

#### API Authorization Token

To utilize the /profiles endpoint within the SecZetta API, you will require an authorization token. To create a new token, navigate to the Admin side of SecZetta -> System -> API. From there, create a new API token and use that in the connector configuration above

#### Profile Type ID

This `profile_type_id` is a value that will be specific to your profiles in your SecZetta environment. Find the id easily by following these steps:

1. Navigate your profile types page in the admin side of SecZetta. (Admin -> Lifecycle -> profile types
1. Select the profile type you want to import into SailPoint
1. Now in the URL you should be able to see the profile_type_id
    a. i.e. <your-seczetta-tenant>/neprofile_admin/profile_types/`687df53e-cdd8-4420-8431-ca6e62e81451`/basic_settings
1. Use that ID in place of <profile_type_id> above

#### Paging Details

The Paging steps listed above is a good working example to get started. If additional detail is needed refer to the Web Services Connector guide in the SailPoint documentation.

The main goal of the paging steps ‘code’ is to allow the web services connector to call SecZetta as many times as required to get the full list of active profiles

```
$sz_limit$ = 100
TERMINATE_IF $RECORDS_COUNT$ < $sz_limit$
$sz_offset$ = $sz_offset$ + $sz_limit$
$endpoint.fullUrl$ = $application.baseUrl$ + "/profiles?profile_type_id=<profile_type_id>&query[limit]=" + $sz_limit$ + "&query[offset]=" + $sz_offset$
```

Initially the limit of 100 would typically work. Sometimes however, the profiles in your SecZetta instances may be full of a large amount of attributes and additional data. In this case, you may want to lower that limit to ensure the API has enough time to download all the profile data without timing out. Play around with the limit variable above to meet your needs

### API Integration (SecZetta Initiated)

For this integration SecZetta will initiate the creation of identities using the /beta/non-employee-records API endpoint.

#### OAuth Client Creation

In the global settings, under security settings is ‘API Mangement’. On this page you are able to create a new OAuth Client by hitting the “+ New” button. Ensure that the client is for ‘Client Credentials’, ‘Refresh Token’, and ‘Authorization Code’. The screenshot below was taken in Q1 of 2021
 
Whenever you create your Client. Make sure to take not of the client_id and more importantly the client_secret. Those will be used to configure the REST API Action in SecZetta

Create a non-employee source (in IDN)

To utilize the API integration, IdentityNow needs to be setup with a non-employee source. You can do this by adding a new source connector. The Source Type for this connector will be ‘Non-employee’.

From here, the /beta/non-employee end point can be used to manage these identities


 
Get SourceID for non-employee Source

In order to create an Identity for the source that was created above. The /beta/non-employee endpoint requires a sourceId for the API call. The way to grab this sourceId is by using the same OAuth client above and calling the {{IDN_API_URL}}/beta/non-employee-sources endpoint.

If done successfully, the response should look very similar to this:

[
    {
        "id": "ac110006-76f4-1acc-8176-f85c7f9e000a",
        "sourceId": "2c91808876f477e60176f85c750b59a6",
        "name": "SecZetta NE",
        "description": "Non Employees From SecZetta",
        "approvers": [
            {
                "type": "IDENTITY",
                "id": "2c91808576774548017686132de3041f"
            }
        ],
        "accountManagers": [
            {
                "type": "IDENTITY",
                "id": "2c91808576774548017686132de3041f"
            }
        ],
        "created": "2021-01-12T20:49:40.26Z",
        "modified": "2021-01-12T20:50:26.823Z",
        "nonEmployeeCount": null
    }
]



Configuring the REST API Action

Within SecZetta, Create and Update workflows will make changes to the SecZetta profiles. These changes will likely result in an create/update required on the IdN side as well. This is where the REST API Action will come into play. Open whichever SecZetta workflow that needs to create an Identity cube and add a REST API Action. The following table shows the parameters required to make the API Action work correctly

Parameter | Description
--------- | --------------
Basic Settings &#8594; Description| 	Create or Update IDN Account
AuthN &#8594; Auth type	| OAuth2
AuthN &#8594; Access token URL | https://`<your-idn-tenant>`.api.identitynow.com/oauth/token

*Notice the api in the URL. That is required
AuthN  Client Id	Client_id for the OAuth Client created above
AuthN  Client secret	Client_secret for the Oauth Client created above
Request  Http verb	POST
Request  Endpoint	https://<your-idn-tenant>.api.identitynow.com/beta/non-employee-records
Request  Headers	Add 2 Headers:
1.	Content-Type = application/json
2.	Accept = */*
Request  Json body	This body will vary depending on the IDN configuration and schema. Here is an example

{
"accountName": "{{attribute.profile_uid_ne_attribute}}",
  "firstName": "{{attribute.personal_first_name}}",
  "lastName": "{{attribute.personal_last_name}}",
  "email": "{{attribute.personal_email}}",
  "phone": "{{attribute.phone_number}}",
  "manager": "john.doe",
  "sourceId": "2c91808876f477e60176f85c750b59a6",
  "data": {
      "riskscore": "6.92"
  },
  "startDate": 1610524800,
  "endDate": 1620892800
}

Notice the sourceId field that is required.

Response  Status Code Mapping	Map this status code to a SecZetta attribute. This will allow error handling within the workflow via conditionals

 

Response  Data Mapping(s)	The API response will contain the IdentityNow ID if the user was created successfully. Make sure to map that ID to a SecZetta attribute. This way during an update/delete, SecZetta will be able to update the identity correctly

 

