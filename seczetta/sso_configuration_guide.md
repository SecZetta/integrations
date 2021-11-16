# SSO Configuration Guide

## Contents

### Setup

#### Configure SecZetta SSO

1. On the `Admin` side of SecZetta: Navigate to System &#8594; Authentication
2. Click the `SSO` tab at the top of the screen
3. Toggle SAML SSO from `OFF` to `ON`
4. Enter the following values into the left half of the page. These values for SP Entity ID and the other attributes are case sensitive and need to be lowercase

Field             | Development    | Test           | Production
------------------|----------------|----------------|----------------
SSO NAME          | Single Sign-On | Single Sign-On | Single Sign-On
SP ENTITY ID      | seczettadev    | seczettatest   | seczettaprod
NAME ATTRIBUTE    | displayname    | displayname    | displayname
EMAIL ATTRIBUTE   | email          | email          | email
GROUPS ATTRIBUTE  | groups         |      groups    | groups

5. Click the `SP SAML Data` button to download the XML metadata file
6. After clicking the button, you will notice two new values appear on the screen, Consumer Service URL and Logout URL. The screen should resemble something like below:

![alt text](img/sso/sso-sp-metadata.png)


#### Configure the Identity Provider

At this point, the Identity Provider (IDP) needs to be configured. Typically our customers are the ones configuring their IDP, so the metadata file downloaded above should be given to the appropriate team on the customer side to allow this configuration to occur. When finished, the customer will return a different metadata file that needs to be imported into SecZetta. See below once you have a new metadata file frome the IDP

#### Import the Identity Provider's Metadata File

1. Save this new metadata file locally before you begin. Then proceed using the following steps
1. On the `Admin` side of SecZetta: Navigate to System &#8594; Authentication
1. Click the `SSO` tab at the top of the screen
1. In the `Identity Provider` section heading. At the very bottom of the page you should see a field labeled `Import File` with a `+` next to the text field. Click that button and browse for your metadata file you saved in step 1.
1. Once imported, the blank fields will show the values contained in the file

#### Confirmation

If a user role has not already been created for Administrators, make one and assign it a Directory group to which an Administrator belongs. Ask the client’s administrator to log in using SSO. If successful, you should see a new user with valid name, email, login, and role(s) as shown in the image below. 

![alt text](img/sso/sso-user-created.png)

### Troubleshooting

#### SAML Assertion

A SAML trace captures the SAML assertion (response) returned to the SecZetta application by the Identity Provider. Ensure a `<NameID>` tag is present. Also check the attributes sent in the `<AttributeStatement>` tag. See below for examples

![alt-img](img/sso/sso-saml-assertion.png)

#### Install a tracer

A trace can only be performed locally, therefore the Administrator asked to test connectivity will need a plugin installed. For Chrome, add an extension like [SAML-tracer](https://chrome.google.com/webstore/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch?hl=en).  

#### Run a trace

Once installed, open the trace window by clicking the extension’s icon  Ask the tester to try to login using SSO. If unsuccessful, take a look at the trace window and locate the row POST https://subdomain.domain.com/saml/consume. Click this row to view the SAML response.

![alt-img](img/sso/sso-saml-tracer.png)

#### Common Problems

Below is a list of some common problems you may see when configuring SSO in SecZetta

1. Atribute Names

Some identity providers pass full schema names instead of short strings, like Email was in the previous example. 

```xml
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress">
        <AttributeValue>John.Doe@email.org</AttributeValue>
    </saml:Attribute>
```

In this event, the SecZetta SSO configuration can be changed to map the Email Attribute to http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress. This can be done for any of the attributes passed.

2. Fingerprint Algorithm

Always check to make sure the fingerprint algorithm matches from SecZetta to the IDP. For example: if the Identity Provider is using RSA-SHA256, make sure that is selected in the Fingerprint Algorithm drop down field.