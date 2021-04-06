# SecZetta / BitSight Integration

## Contents

- [SecZetta / BitSight Integration](#seczetta---bitsight-integration)
  - [Overview](#overview)
    - [Architecture Overview](#architecture-overview)
  - [Supported Features](#supported-features)
  - [Prerequisites](#prerequisites)
    - [Examples](#examples)
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

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Overview

Organizations are often in the dark when it comes to understanding the actual security performance of critical third parties or even assessing the impact of their own security programs and policies. This is due to a lack of objective metrics and tools that help measure and mitigate cyber risk across the business ecosystem.

BitSight pioneered the security ratings market, founding the company with a solitary mission: to transform how organizations evaluate risk and security performance by employing the outside-in model used by credit rating agencies.

SecZetta is able to utilize this robust cyber risk data to apply directly to not only organizations but to apply that risk to the underlying identities associated with those organizations. This allows our customers to use this risk data inside SecZetta workflows and also passed down to our other partner integrations (IAM / PAM)

The below diagram gives a high level architecture diagram

### Architecture Overview

![Image of Risk Rank](https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/bitsight-integration-overview.png)

- Step 1: Call BitSight to grab all companies risk ratings
- Step 2: BitSight responds back with the risk ratings
- Step 3: Proxy Job server analyzes risk rating and normalizes risk score to pass to SecZetta
- Step 4: Proxy Job server pushes risk data to Vendor profiles
- Step 5: Success response sent back



## Supported Features

- Sync BitSight risk rating to SecZetta

## Prerequisites

1. An active SecZetta account and tenant where you have administrative privileges. To set up a new SecZetta account, please reach out to [SecZetta Support (info@seczetta.com)](mailto:info@seczetta.com)

2. An active SecZetta API Token

3. The Vendor/Org Profile Type ID

4. BitSight Environment with administrative access

5. BitSight Token (to use the API)

### Examples

> The SecZetta Instance URL will be in this format: `https://<seczetta-tenant>.mynonemployee.com`.

> Example SecZetta API Token: `c7aef210f92142188032f5a7b59ed0f6`

> Example Vendor Profile Type ID: `47826aa2-ada3-4077-82ac-e90b4a8ce910`

> Example BitSight token: `e45b46958ece37895493f3811422569a61196760`

### Generating a SecZetta API Key

In order to generate an API Key follow these steps: 

1. Navigate to the [admin](#seczetta-admin-dashboard) side of SecZetta (NEProfile dashboard). 

2. Click into [`System -> api`](#seczetta-api-page)

3. Click the `+ Api Key` button and copy your API Key

#### SecZetta Admin Dashboard
<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/seczetta-dashboard-admin-button.png" width="50%"/>

#### SecZetta API Page

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/bitsight-navigate-to-account.png" width="50%"/>

### Getting BitSight API Token

1. Login to your BitSight tenant and navigate to your `account settings`

2. Scroll down until you see the API Token section and generate a new API token

#### Account Dropdown

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/seczetta-api-keys.png" width="50%"/>

#### Generate BitSight API Key

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/bitsight-api-token.png" width="50%"/>

## Configuration

As described above in the high level [architecture](#architecture-overview), the BitSight integration runs on the Proxy Job Server. The script [sync-bitsight-risk-ratings.rb](sync-bitsight-risk-ratings.rb) is a Ruby script that will be scheduled to keep SecZetta up to date.

Before executing the script import the [`init-bitsight.json`](init-bitsight.json) file. This file imports the specific bitsight attributes that the script is looking for as well as creates helpful forms to be able to use on your vendor profile types

### SecZetta Objects

#### Attributes

The [`init-bitsight.json`](init-bitsight.json) file will import the following attributes:

Attribute UID | Attribute Label | Description | Example Value
--------------|-----------------|-------------|----------------
bitsight_integrated_security_rating | Integrated Security Rating | Scaled Risk Ranking (0 - 10) | 5.5
bitsight_rating_date | BitSight Rating Date | Date last rated | 04/05/2020
bitsight_rating | Bitsight Rating | Full Bitsight Rating (250 - 900) | 470
bitsight_guid | BitSight UID | Unique identifier used to sync Vendors | 2bd2cbb2-e4b8-4259-95d1-f562c731d5c8
bitsight_full_vendor_risk_assessment_complete | Risk Assessment Complete | Flag showing if a full assessment has been performed | Yes

#### Form



### Integration Script

On lines 8 - 15 of the [sync-bitsight-risk-ratings.rb](sync-bitsight-risk-ratings.rb) script, will be the only change you need to make to the script itself.

```ruby 
$NE_TOKEN = 'c7aef210f92142188032f5a7b59ed0f6'
# Your BitSight Token
$BS_TOKEN = 'e45b46958ece37895493f3811422569a61196760'
# Your SecZetta Tenant URL
$NEP_URL = 'https://<seczetta-tenant>.mynonemployee.com'
# Profile Type ID for your Vendors
VENDOR_ID = "47826aa2-ada3-4077-82ac-e90b4a8ce910"
```

Make sure to update these 4 variables in order to have the script operate properly

## API Usage

### BitSight API

The script works as expected without the need to fully understand the API; however if extra details/data is required to be sync'd to SecZetta it is helpful to understand the BitSight API. The next few sections describe the API in detail.

#### Authentication

The BitSight API uses a token-based authentication. Use an Authentication Type of `Basic` if you are setting up something like Postman to begin testing the API out.

Make sure to put the BitSight API Token in as the username and leave the **password field blank**

<img src="https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/bitsight-postman-get-risk-data.png" width="50%"/>

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

> The API will respond back with a `200 OK` if the request was succesful