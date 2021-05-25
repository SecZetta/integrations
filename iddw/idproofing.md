- [Identity Proofing User Guide](#identity-proofing-user-guide)
  * [SecZetta Identity Proofing](#seczetta-identity-proofing)
    + [Identity Proofing](#identity-proofing)
    + [Goal of the Document](#goal-of-the-document)
  * [Understanding the Tool](#understanding-the-tool)
  * [Before Using the System](#before-using-the-system)
    + [SMS Cabable Device - Mobile Match and Government ID Verification](#sms-cabable-device---mobile-match-and-government-id-verification)
    + [Mobile Support - Government ID Verification](#mobile-support---government-id-verification)
    + [Recommended Browsers - Government ID Verification](#recommended-browsers---government-id-verification)
    + [Supported Document Types - Government ID Verification](#supported-document-types---government-id-verification)
  * [Using the System](#using-the-system)
      - [In the browser](#in-the-browswer)
    + [Mobile Match](#mobile-match)
    + [Government ID Verification](#government-id-verification)
      - [On Your Device](#on-your-device)
    + [Mobile Match fail over to Government ID Verification](#mobile-match-fail-over-to-government-id-verification)
  * [Troubleshooting](#troubleshooting)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Identity Proofing User Guide

## SecZetta Identity Proofing

As enterprise organizations increasingly grant access to facilities, data, and systems to an ever-expanding number of third-party users, it becomes imperative for them to prove that these people are in fact who they claim to be.  

### Identity Proofing

With SecZetta’s Identity Proofing it’s possible to easily invoke large scale or individual identity verification during the onboarding process or at any time throughout the identity lifecycle. 

### Goal of the Document

This document is designed to familiarize users with Identity Proofing features and functionality.


## Understanding the Tool

Identity Proofing can be configured to leverage mobile carrier records and/or the combination of a government issued photo ID (see below) and a live selfie to confirm that users are who they claim to be.  A user may be prompted to prove their identity during onboarding or at any point during their lifecycle.  



## Before Using the System

There are two available methods of Identity Proofing withing SecZetta: **Mobile Match** and **Government ID Verification**. Before you begin using Identity Proofing, please ensure you understand which way you'll be asked to verify your identity and ensure you'll be able to meet system requirements below: 

### SMS Capable Device - Mobile Match and Government ID Verification
You will need to be able to receive SMS messages so you will need to have a device capable of receipt and enough service to receive.

### Mobile Support - Government ID Verification

Mobile support does not require a special application.  You will need a mobile device with a camera, and access to a mobile browser.  Please see below for further details on compatibility:

|Device Type |OS Version            |Release Date  |
|:-----------|:---------------------|--------------|
|Android	   |5.0 Lollipop or newer |November 2014 |
|iOS	       |12.0 or newer         |September 2018|


### Recommended Browsers - Government ID Verification

|Device Type |Recommended Browser|
|:-----------|-------------------|
|Android     |Chrome             |
|iOS		     |Safari             |


### Supported Document Types - Government ID Verification

Below are the types of documents that can be leveraged to verify user identity details with the Government ID flow.  This service works for roughly 200 countries and 5000 specific types of documents. 

|Document Type           |Supported?|
|:-----------------------|:---------|
|Unknown	               |No        |
|Passport                |Yes       |
|Visa                    |Yes       |
|Drivers License	       |Yes       |
|Identification Card     |Yes       |
|Permit           	     |Yes       |
|Currency	               |No        |
|Residence Document      |No        |
|Travel Document         |Yes       |
|Birth Certificate 	     |No        |
|Vehicle Registration    |No        |
|Other	                 |No        |
|Weapon License          |No        |
|Tribal Identification   |No        |
|Voter Identification    |No        |
|Military	               |Yes       |
|Consular Identification |Yes       |


## Using the System

Identity Proofing will either be initiated as part of an onboarding workflow or you will be contacted to verify your identity by the organization that holds your profile.  Either way, you will be directed to a page within SecZetta where you will select to begin the identity proofing process.

#### In the browser

- **Click 'Verify My Identity'**
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/81b5395408fbbc092960212754532fce123a2391/img/Screen%20Shot%202021-05-10%20at%208.41.38%20PM.png" width="50%"/>



- **Select your country**

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/ea442120a1cf09dfb35cfcd1175db7e312d753e9/img/Screen%20Shot%202021-05-10%20at%208.41.59%20PM.png" width="30%"/>



At this point there are 3 potential verification processes that you may encounter:

1. Mobile Match
2. Government ID Verification
3. Mobile Match fail over to Government ID Verification

Each will be outlined below.

### Mobile Match

- **Enter your mobile phone number and home address** and then **click on Confirm Information**

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/d4b40be586fda0346f7c73c55c27902b125a8096/img/Enter%20Address%20and%20Phone.png" width="30%"/>



- **Select SMS or Voice** for your preferred method to receive a one time PIN

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/d4b40be586fda0346f7c73c55c27902b125a8096/img/PIN%20Delivery%20Method.jpg" width="30%"/>



- If you selected to receive your PIN via SMS, go to your messages on your mobile device and **find the SMS containing your PIN** 

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/d4b40be586fda0346f7c73c55c27902b125a8096/img/SMS.jpg" width="30%"/>



**OR**


- If you selected to receive your PIN via Voice, you'll want to answer your phone and **note the PIN as it is read to you on the call**



- **Enter your PIN** and then **click on Confirm Information**

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/d4b40be586fda0346f7c73c55c27902b125a8096/img/Confirm%20PIN.png" width="30%"/>

- You will now be redirected via the browser to **view your Identity Verification results**.



### Government ID Verification

- **Select the type of identification** that you'd like to use during the verification process

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/c79fbe9e78f6722b24b6fb8d6c222c036454c346/img/Screen%20Shot%202021-05-10%20at%208.42.26%20PM.png" width="30%"/>



- **Enter your mobile number** where you wish to receive the SMS notification for continuing with the image capture process

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/c79fbe9e78f6722b24b6fb8d6c222c036454c346/img/Screen%20Shot%202021-05-10%20at%208.42.54%20PM.png" width="30%"/>



- When you are redirected to your phone, **DO NOT** close your browser window.  You will come back here to complete the verification.

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/c79fbe9e78f6722b24b6fb8d6c222c036454c346/img/Screen%20Shot%202021-05-10%20at%208.43.14%20PM.png" width="30%"/>


#### On Your Device

- **Click on the link within the SMS message**
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/1eca0f225fcb9eae2710d35c8e417cf7bbaebfb2/img/SMS.jpg" width="30%"/>



- After reviewing directions **Click 'Start'**
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/00becd908fb3607babebc5cb8ebe41b899fd02db/img/Begin%20capture%20process.png" width="30%"/>



- Follow on screen prompts and **Click 'Capture Using Your Browser Camera'**
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/848a7d5add8d1fda1dae36edfe3130373e61d927/img/Front%20ID%20Image.png" width="30%"/>


- **Allow the application to access the camera**. The verification requires no special apps to be installed, but in order to successfully capture images of your ID and your selfie you will have to grant temporary access to the camera via your mobile browser.
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/848a7d5add8d1fda1dae36edfe3130373e61d927/img/Allow%20Camera%20Access.jpg" width="30%"/>


- **Capture Image**.  If you choose to use a drivers license or ID this will be the image of the front of your ID.  If you are using your passport this will be the image of the photo page.  Follow on screen prompts to properly align the image and verify image meets requirements before submitting.  If your image does not meet one of the requirements please review the [Tips and Tricks](https://github.com/cchristensen-sz/IdentityProofing/blob/cac396a002e52069745c8147ce5fbf471945b1ac/img/tips_and_tricks.pdf) document and try again.  Once all requirements have been met, **Click 'Save and Next'**
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/0b5c9132b7c0bf4eb5eff3fdd8bf766fa171059c/img/Front%20of%20ID.png" width="30%"/> 


- If you choose to use an ID or a drivers license, you will now begin the process of capturing the image of the back of the document. **CLick on 'Capture Using Your Browser Camera'** to take the second photo.
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/38de26c7dace4fa4754aff8db93700bd35399abe/img/Back%20of%20ID%20start.png" width="30%"/>

- Capture the image with on screen guidance

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/38de26c7dace4fa4754aff8db93700bd35399abe/img/Back%20of%20ID%20Submit.png" width="30%"/>

- Once an acceptable image has been captured, **Click 'Save and Next'**

- **Capture Seflie** by following on screen prompts.  **Click 'Capture Using Your Phone Camera'**. Once captured if the image is acceptable, you will be redirected back to the browser window where the ID Proofing process was initiated.
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/1e64e168db0311151a92167f2bed709fddabf636/img/Selfie%20Start.png" width="30%"/>

- Smile!

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/ebf63167829f016ac82e3d0075da6277a1a077ac/img/Selfie.png" width="30%"/>

- Once you submit your images and see this screen you can pick up the process in your original browser window.

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/1e64e168db0311151a92167f2bed709fddabf636/img/Selfie%20Submit.png" width="30%"/>

- Ensure that you see the results from your proofing activity.  You have completed Government ID verification!

<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/b4dd27657f7be4a75696ee6855fee44bf285469f/img/Proofing%20completion%20.png" width="30%"/>

### Mobile Match fail over to Government ID Verification
- This workflow is a combination of Mobile Match and Government ID Verification.  You will:
-  **Select Your Country**
-  If you are US based, you will proceed to the [Mobile Match workflow](https://github.com/cchristensen-sz/IdentityProofing#mobile-match).
-  If you pass the mobile match workflow, your verification is complete
-  If SecZetta is unable to verify your identity via Mobile Match you will proceed to the [Government ID Verification workflow](https://github.com/cchristensen-sz/IdentityProofing#government-id-verification)
<img src="https://github.com/cchristensen-sz/IdentityProofing/blob/d4b40be586fda0346f7c73c55c27902b125a8096/img/Unable%20to%20prove%20your%20Identity.png" width="30%"/>
-  Once completed you will be returned to the browser you initiated proofing from, and your results will be displayed.

## Troubleshooting 

If you run into challenges, the following should be attempted before contacting support:

- Ensure you have sufficient service

- Ensure your use case meets requirements listed [HERE](https://github.com/cchristensen-sz/IdentityProofing/blob/main/README.md#before-using-the-system)

- For challenges during the Government ID Verification process please reference this [Tips and Tricks](https://github.com/cchristensen-sz/IdentityProofing/blob/cac396a002e52069745c8147ce5fbf471945b1ac/img/tips_and_tricks.pdf) document.

- Ensure you have sufficient battery on your device or that you are plugged in.

- Close other open mobile browser windows.

