
# Coming Soon!

# Instructions

* Please copy this template (copy either the markdown by clicking **Raw** or the copy directly from this preview) and use it to create your guide in your preferred medium. 
* This template includes information required in all SecZetta integration guides.
* Template instructions in ***bold italics*** are intended to provide guidance or examples, and should be deleted and/or replaced once you’ve added your content.
* If your integration does not follow the same flow as what we’ve provided below (e.g. steps begin in your tool’s UI as opposed to the SecZetta UI, etc.), feel free to make the changes you need to reflect the flow of the integration.
* Please read through our Writing and Style Guidelines below before starting your draft.

# Writing and Style Guidelines

## Detailed, Explicit Instructions

All steps to completing the integration should live in this guide. It's always good to err on the side of too much information, even if you think something is obvious. By writing your instructions as if the reader has had zero experience with any of the content, you can proactively anticipate any customer questions and greatly relieve Support efforts. 

**Example**:

* **Don't**: "Find your ClientID and paste it into this field."

* **Do**: "Navigate to **Account Settings** in the system menu and copy your **Client ID**. Next, navigate back to the **Configuration** page and paste it in the **ID** field."

## Calls to Action

Most calls to action include clickable objects or fields, which you should highlight with **bold text**. This helps the reader follow along in the instructions and denotes when they should be taking action in the UI. 

**Examples**:

* "Navigate to the **Configuration** menu and select **Users**."

* "Paste the **Integration Key** into the **Token** field"

## Actionable Steps

Summaries before your content may work well when giving a talk or presenting to a targeted crowd, but not in documentation that users are more likely to skim hoping for quick answers. TL;DR: Don't include sentences that just state what you plan on writing about. If you feel you need to add more information that contextualizes what the reader is configuring, include it within the steps, or in a quick summary after them. 

**Example**

* **Don't**: "In this procedure we will be creating a Topic and a Subscription that will then allow you to create messages that trigger SecZetta incidents..." etc.

* **Do**: "1. Navigate to the **Admin** dashboard and click **Templates**. 2. Then **Pages**, configure your page and click **Save**. You have now edited a page that can be used in a SecZetta workflow"

## Use Active Voice

The active voice ensures that your writing is clear, concise and engaging. The [passive voice](https://webapps.towson.edu/ows/activepass.htm) uses more words, can sound vague and should be avoided like a [zombie plague](https://www.grammarly.com/blog/a-scary-easy-way-to-help-you-find-passive-voice/) (rhyme intended).

**Example**

* **Do**: "Users can follow incidents and escalations in real-time in Hungrycat’s event stream."
* **Don't**: "Incidents and escalations can be followed in real-time by users in Hungrycat’s event stream."

## Media

* At SecZetta, we use the Preview tool that comes standard on macOS. Type **⌘ + ⇧ + A** or click **View** > **Show Markup Toolbar** to annotate images with arrows, rectangles and text.
* Only include screenshots that are **absolutely necessary**, so that you have less images to continually update when UI changes, etc. We usually only include screenshots when objects in the UI are small or harder to find. 
* Ensure that you've obfuscated all sensitive information in your screenshots (e.g., personal account information, integration keys, etc.,) by covering with fake data or an image blur tool. 

^^^ Note: Once you have completed your guide, please delete this section. ^^^
----

# SecZetta / <Product-Name> Integration

## Contents

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Overview

Give a brief overview of what the product does

### Architecture Overview

#### EXAMPLE: 

![Image of Risk Rank](https://raw.githubusercontent.com/SecZetta/integrations/main/bitsight/img/bitsight-integration-overview.png)

- Step 1: Call BitSight to grab all companies risk ratings
- Step 2: BitSight responds back with the risk ratings
- Step 3: Proxy Job server analyzes risk rating and normalizes risk score to pass to SecZetta
- Step 4: Proxy Job server pushes risk data to Vendor profiles
- Step 5: Success response sent back



## Supported Features

- List supported features
- here

## Prerequisites

Almost all integrations will have the first 2 prereq.

1. An active SecZetta account and tenant where you have administrative privileges. To set up a new SecZetta account, please reach out to [SecZetta Support (info@seczetta.com)](mailto:info@seczetta.com)

2. An active SecZetta API Token

3. Any other prereqs

### Examples

> The SecZetta Instance URL will be in this format: `https://<seczetta-tenant>.mynonemployee.com`.

> Example SecZetta API Token: `c7aef210f92142188032f5a7b59ed0f6`

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

As described above in the high level [architecture](#architecture-overview), describe the techincal integration briefly

> Make sure to list all the steps required to setup the config

### Integration Script (if required)

## API Usage (if required)

### <Product Name>  API

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

> The API will respond back with a `200 OK` if the request was successful
