# SecZetta / PingOne Integration

## Contents

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Overview

PingOne® for Enterprise is a fast, simple and easy identity-as-a-service (IDaaS) single sign-on (SSO) offering that enables enterprises to give their users federated access to applications with a single click from a secure, cloud-based dock, accessible from any browser or mobile device. PingOne for Enterprise reduces user password sprawl and improves user experience, all while improving business agility and driving administrative efficiency.

The PingOne for Enterprise platform makes it easy for administrators to connect to cloud applications via PingOne Application Catalog integrations to popular SaaS applications such as Microsoft Office 365, Salesforce.com, Google and more. Admins can also easily leverage secure identity standards such as SAML and OIDC to integrate a wide range of other cloud applications quickly and seamlessly. Several options are available for PingOne for Enterprise to connect to identity providers, such as Active Directory, to authenticate users. Administrators are provided with the option to keep their identity data with their preferred identity provider or store it in PingOne’s cloud directory.

PingOne for Enterprise is architected to scale; some of our enterprise customers have connected 2,000+ applications to their PingOne for Enterprise accounts. With high availability and performance, PingOne for Enterprise reliably delivers secure IDaaS solutions for the enterprise.

### Architecture Overview

#### EXAMPLE: 

![Image of Architecture Overview](https://raw.githubusercontent.com/SecZetta/integrations/main/pingone/img/pingone-architecture-overview.png)

- Step 1: SecZetta will launch a lifecycle workflow for a profile.
- Step 2: Based on the result of this workflow, SecZetta will send off the correct requests to PingOne. The following PingOne integration options are supported:
  - Create new directory account
  - Update existing account
  - Add/Remove group memberships
  - Enable/Disable account
- Step 3: Will only execute if creating an account is required
- Step 4: Will execute if a user requires updating or needs to be enabled/disabled
- Step 5: Will execute for any group membership changes
- Step 6: Success response sent back

## Supported Features

- Create new PingOne directory account
- Update existing PingOne directory account
- Add/Remove users from PingOne groups
- Enable/Disable PingOne directory account

### Coming Soon

- Webhook integration

## Prerequisites

1. An active SecZetta account and tenant where you have administrative privileges. To set up a new SecZetta account, please reach out to [SecZetta Support (info@seczetta.com)](mailto:info@seczetta.com)

2. An active SecZetta API Token

3. An active PingOne for Enterprise account with Administrative access

4. PingOne API Credentials ( SETUP -> Directory -> API Credentials)

### Examples

> The SecZetta Instance URL will be in this format: `https://<seczetta-tenant>.mynonemployee.com`.

> Example SecZetta API Token: `c7aef210f92142188032f5a7b59ed0f6`

> Example PingOne API Credentials:\
> PingOne Client-ID: `9fe3f802-4bf5-4f1c-8032-0ce48abdbe34`\
> PingOne API Key: `iriC9lvZGxI3y5tlJgAnMjD2y725OZ`

### Generating a SecZetta API Key

In order to generate an API Key follow these steps: 

1. Navigate to the [admin](#seczetta-admin-dashboard) side of SecZetta (NEProfile dashboard). 

2. Click into [`System -> api`](#seczetta-api-page)

3. Click the `+ Api Key` button and copy your API Key

#### SecZetta Admin Dashboard

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/seczetta-dashboard-admin-button.png" width="50%"/>

#### SecZetta API Page

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/bitsight-navigate-to-account.png" width="50%"/>

## Configuration

As described above in the high level [architecture](#architecture-overview), the integration deals mostly with REST API calls from SecZetta to PingOne. This is done using the REST API Action in any SecZetta workflow. 


## API Usage (if required)

### <Product Name>  API

#### Authentication

The PingOne API uses basic authentication using an Client-Id and API Key. Use an Authentication Type of `Basic` if you are setting up something like Postman to begin testing the API out.

Make sure to put the BitSight API Token in as the username and leave the **password field blank**

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/pingone/img/pingone-postman-example.png" width="50%"/>

#### GET /ratings/v1/companies

The only API endpoint required on the BitSight side is the `/ratings/v1/companies` endpoint. This endpoint pulls the risk ranking details that will be synced to SecZetta. See below for an example response.

The key data points that are synced to SecZetta are `rating`, `rating_date`, `guid`. The full rating gets synced to SecZetta; however the script also normalizes the rating on to a 0 - 10 scale.

BitSight operates on a 250 - 900 scale. Here is an example of that scale in action:

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/bitsight-risk-example.png" width="50%"/>

##### Example Scale

Here are a few examples to see how that rating scales

BitSight Rating (250 - 900) | ==> | Integrated Security Rating (0 - 10)
------------ | -- | -------------
470|==>|3.4
740|==>|7.5
760|==>|7.8
320|==>|1.1
380|==>|2.0
480|==>|3.5
500|==>|3.8
360|==>|1.7
410|==>|2.5
720|==>|7.2
460|==>|3.2
480|==>|3.5
750|==>|7.7
370|==>|1.8
640|==>|6.0
320|==>|1.1


##### Example JSON Response

```json

"created": "2018-11-12",
    "rating_date": "2021-03-29",
    "companies": [
        {
            "guid": "a940bb61-33c4-42c9-9231-c8194c305db3",
            "custom_id": null,
            "name": "Saperix, Inc.",
            "shortname": "Saperix",
            "network_size_v4": 5273,
            "rating": 470,
            "rating_date": "2021-03-29",
            "date_added": "2018-11-12",
            "industry": "Technology",
            "industry_slug": "technology",
            "sub_industry": "Computer & Network Security",
            "sub_industry_slug": "computer_network_security",
            "type": "CURATED",
            "logo": "<logo-url-redacted>",
            "sparkline": "<sparkline-url-redacted>",
            "external_id": 14885770,
            "subscription_type": "Total Risk Monitoring",
            "subscription_type_key": "continuous_monitoring",
            "primary_domain": "saperix.com",
            "security_grade": null,
            "grade_date": null,
            "display_url": "<display-url-redacted>",
            "href": "<href-url-redacted>"
        },
        // more companies...
    ]
```

> The API will respond back with a `200 OK` if the request was successful
## Example Create User 

### API Call

> POST https://directory-api.pingone.com/api/directory/user

### Body

```json
{
    "schemas": [
        "urn:scim:schemas:core:1.0"
    ],
    "userName": "john.doe",
    "password": "2Federate",
    "active": true,
    "name": {
        "familyName": "Jonathan",
        "givenName": "Doe"
    },
    "emails": [
        {
            "type": "work",
            "value": "John.Doe@pingdevelopers.com"
        }
    ]
}
```

### Response

```json
{
    "emails": [
        {
            "type": "work",
            "value": "john.doe@pingdevelopers.com"
        }
    ],
    "meta": {
        "created": "2021-04-05T07:58:03.958-06:00",
        "location": "https://directory-api.pingone.com/v1/user/f2b57921-cbd5-4941-a549-1b610e17bbfe",
        "lastModified": "2021-04-05T07:58:03.958-06:00"
    },
    "schemas": [
        "urn:scim:schemas:core:1.0",
        "urn:scim:schemas:internal:1.0",
        "urn:scim:schemas:com_pingone:1.0"
    ],
    "name": {
        "givenName": "Doe",
        "familyName": "Jonathan"
    },
    "groups": [],
    "active": true,
    "id": "f2b57921-cbd5-4941-a549-1b610e17bbfe",
    "userName": "john.doe",
    "urn:scim:schemas:com_pingone:1.0": {
        "lastModifiedTimeStamp": 1617631083958,
        "accountId": "8dd3f802-4bf5-4f1c-8032-0ce48abdbe34",
        "createTimeStamp": 1617631083958,
        "directoryId": "cae28685-78b4-4dd6-bc5e-620a1d611d4d",
        "state": "ACTIVE"
    }
}
```

## Example Add/Remove User from group

