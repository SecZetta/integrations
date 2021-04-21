# SecZetta / Cyberark Alero Integration

## Contents

- [SecZetta / Cyberark Alero Integration](#seczetta---cyberark-alero-integration)
  * [Contents](#contents)
  * [Overview](#overview)
    + [High Level Diagram](#high-level-diagram)
  * [Supported Features](#supported-features)
  * [Prerequisites](#prerequisites)
    + [Examples](#examples)
  * [Configuration](#configuration)
    + [Creating the REST API Action](#creating-the-rest-api-action)
      - [Authentication Attributes](#authentication-attributes)
      - [Request Attributes](#request-attributes)
        * [JSON Body](#json-body)
  * [Putting it all together](#putting-it-all-together)
  * [Potential Improvements](#potential-improvements)
    + [Invitation ID Response Text](#invitation-id-response-text)
    + [InvitationId and VendorId](#invitationid-and-vendorid)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Overview

CyberArk Remote Access (formerly Alero™) combines Zero Trust access, biometric multi-factor authentication and just-in-time provisioning into one SaaS-based offering. Remote Access is designed to provide fast, easy and secure privileged access to 3rd party vendors who need access to critical internal systems via CyberArk, without the need to use passwords. By not requiring VPNs or agents Remote Access removes operational overhead for administrators, makes it easier and quicker to deploy and improves organizational security.

SecZetta's integration into Cyberark Remote Access is focused on the onboarding / offboarding of all non-employees that SecZetta is managing. The SecZetta onboarding process can be minimally changed to add extra steps to automatically send out CyberArk Remote Access invitiations. This will ensure your vendors have the ability to securely RDP into the proper environment securely.

### High Level Diagram

![CyberArk Alero](img/cyberark-alero-overview-diagram.png)

- Step 1: Approved Non-employee is created inside SecZetta
- Step 2: SecZetta communicates with CyberArk to send off invitation to this newly created non-employee
- Step 3: CyberArk responds back with a 200 OK Success message
- Step 4: CyberArk sends out email/phone notification to non-employee
- Step 5: Non-employee registers his/her CyberArk Remote Access account and is able to start work

## Supported Features

- Automatically trigger CyberArk Remote Access email notifications

> Coming Soon (waiting on CyberArk API improvements): 
> - Disable outstanding invitations on offboarding
> - Disable CyberArk Remote Access account (if required) during offboarding

## Prerequisites

1. An active SecZetta account and tenant where you have administrative privileges. To set up a new SecZetta account, please reach out to [SecZetta Support (info@seczetta.com)](mailto:info@seczetta.com)

2. An active SecZetta API Token

3. Any other prereqs

4. CyberArk Remote Access service account and private key (for calling the CyberArk API)

> See CyberArk's API Documentation Here: https://api.alero.io/swagger-ui.html#/

### Examples

> The SecZetta Instance URL will be in this format: `https://<seczetta-tenant>.mynonemployee.com`.

> Example SecZetta API Token: `c7aef210f92142188032f5a7b59ed0f6`

## Configuration

The configuration on the SecZetta side is all inside workflows using the REST API action. CyberArk has an api endpoint for sending out vendor invites and managing those invites after the fact (e.g. `https://api.alero.io/v1-edge/invitations/vendor-invitations`)

For documentation purposes no approvals or extra SecZetta workflows will be shown, but understand that all of these extra features can be layered on top of this integration.

There is also a powerpoint script that CyberArk provides its partners/customers that might be useful for those who want to dig deeper into the technical side of the integration. See that script in the repo [here](alero-helper.ps1)

### Creating the REST API Action

For CyberArk, the `OAuth2 w/private key jwt` authentication option will be used to call the API endpoint. Assuming you have the required pre-requisites, the configuration is very simple.

#### Authentication Attributes

| Attribute        | Value |
|------------------|-------|
| Auth Type        | OAuth2 w/private key jwt |
| Access token url | https://auth.alero.io/auth/realms/serviceaccounts/protocol/openid-connect/token |
| Private key      | `Private Key Redacted` |
| Encryption type  | RS256 |
| Iss              | 11eaab2250acefe0b97f95ccc5c5e407.11eb25ce2fcb389daba55df479a966a3.ExternalServiceAccount |
| Sub              | 11eaab2250acefe0b97f95ccc5c5e407.11eb25ce2fcb389daba55df479a966a3.ExternalServiceAccount |
| Aud              | https://auth.alero.io/auth/realms/serviceaccounts |

> Note the private key should be given to you by CyberArk and will be in start with `-----BEGIN RSA PRIVATE KEY-----`

#### Request Attributes
| Attribute | Value                                                       |
|-----------|-------------------------------------------------------------|
| HTTP verb | POST                                                        |
| Endpoint  | https://api.alero.io/v1-edge/invitations/vendor-invitations |
| Header 1  | Content-Type = application/json                             |
| Header 2  | accept = */*                                                |
| Json Body | See below                                                   |

##### JSON Body 

```json
{
  "accessEndDate": 0,
  "accessStartDate": 0,
  "applications": [
    {
      "applicationId": "11eab4cd6bf27b0f9327cf43487da52e",
      "siteId": "11eaab2463a4d3399816d3b7450c5b10"
    }
  ],
  "comments": "ex.comments",
  "companyName": "{{attribute.vendor}}",
  "emailAddress": "{{attribute.personal_email}}",
  "firstName": "{{attribute.first_name_ne_attribute}}",
  "initialStatus": "Activated",
  "invitedVendorsInitialStatus": "Activated",
  "lastName": "{{attribute.last_name_ne_attribute}}",
  "maxNumOfInvitedVendors": 0,
  "phoneAndEmailAuth": true,
  "phoneNumber": "+1{{attribute.mobile_phone_number_ne_attribute}}",
  "provisioningGroups": [
    "11eacd00e5d4e488baa5514eb0311de7"
  ],
  "provisioningType": "ProvisionedByAlero",
  "provisioningUsername": "{{attribute.first_name_ne_attribute}}.{{attribute.last_name_ne_attribute}}",
  "role": "Vendor"
}
```

> Note: The applicationId, siteId and provisioningGroups will be environment specific. Work with the CyberArk administrator to understand how to set these values. Also, the `phoneNumber` attribute has to include the country code.

## Putting it all together

Now that the REST API action is setup correctly, drop that action into any create workflow on the SecZetta side. This example workflow shown below is available via import file located [here](init-cyberark.json)

![Workflow](img/cyberark-alero-example-workflow.png)

As shown above, there is a very simple workflow:

1.  Request Form: Shows the user a from to onboard this new non-employee. This form also includes a question attribute that asks the user if this non-employee needs Remote Access.

2. Create: Creates the initial SecZetta profile

3. If the user needs remote access, the workflow shows another form to grab their mobile phone number and asks CyberArk to send them an invitation via that REST API Action configured just like above

## Potential Improvements

### Invitation ID Response Text
Whenever the `/vendor-invitations` endpoint is called a non-JSON response is handed back. The response is just a raw text field containing the `invitationId`. It looks something like this: 

```
 11eba29cf4a601b08dbdad6a70500894
```

We have talked with CyberArk about updating this to valid JSON, at the very least wrap it in brackets. But ideally it is appended with `invitationId`. Something like this:

```json
{
  "invitationId": "11eba29cf4a601b08dbdad6a70500894"
}
```

As of Q2 2021, this has not been changed. This also causes problems inside SecZetta, because SecZetta requires JSON responses.

### InvitationId and VendorId

Also, as of right now, the `/vendor-invitations` endpoint returns the invitationId. This ID is valid as long as the invitation is valid. Whenever a user accepts and invitation this ID is no longer useful. It would be nice if the API returned some sort of userID as well as the InviteID so SecZetta would be able to still map a CyberArk Remote Access user appropriately.

