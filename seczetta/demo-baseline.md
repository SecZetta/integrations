# SecZetta - Demo Baseline

## Contents

- [SecZetta - Demo Baseline](#seczetta---demo-baseline)
  * [Introduction](#introduction)
  * [Getting Started](#getting-started)
  * [Demo Script](#demo-script)
    + [Onboarding a new Contractor](#onboarding-a-new-contractor)
      - [Identify Proofing (if applicable)](#identify-proofing--if-applicable-)
      - [Continue with Onboarding](#continue-with-onboarding)
    + [Revalidate an existing profile](#revalidate-an-existing-profile)
    + [Terminate a profile](#terminate-a-profile)
    + [Make Collaborator](#make-collaborator)
    + [Add a new Vendor](#add-a-new-vendor)
    + [Add a new Project](#add-a-new-project)
  * [Workflows](#workflows)
  * [Attributes](#attributes)
  * [Permissions (User Roles)](#permissions--user-roles-)

## Prerequisites

This documentation assumes you have completed the following prerequisites
* [SecZetta 101 - Foundational Overview](https://seczetta.sharepoint.com/sites/PartnerEnablement/SitePages/Sales-101.aspx)
* [SecZetta 201 - Technical Overview](https://seczetta.sharepoint.com/sites/PartnerEnablement/SitePages/Technical-201.aspx)
* [SecZetta 301 - Basic Training](https://seczetta.sharepoint.com/sites/PartnerEnablement/SitePages/Training.aspx)

## Introduction

This baseline is what our presales team uses as a *standard* demo we would give to our clients. This baseline includes three (3) different profiles types: People, Vendors, Projects. The use case is the typcial contractor onboarding flow that our customers utlize the tool to solve.

This demo baseline will give you a good insight into how to configure SecZetta in order to solve some of your customer's non-employee problems. The primary purpose of this documentation is to outline what is built and how to make adjustments if required. There are two Organizations that will be mentioned throughout the documentation and in the tool itself.

* **Z Corp:** This is the organization that is using SecZetta to manage their non employees.
* **Acme Consulting:** This is the third party organization that is doing work for Z Corp.

## Getting Started

The first thing you need to get started is a SecZetta instance with the demo baseline installed. The two (2) urls you will need are below:

* Lifecycle: `https://<your-instance-id>.mynonemployee.com/`
* Collaboration: `https://<your-instance-id>.mynonemployeeportal.com/contractors/`

> Notice the difference in the domains between Lifecycle and Collaboration. One is mynonemployee.com the other is mynonemployeeportal.com. This just signifys which module you are utilizing

The easiest way to onboard new people is by using the Contractors collaboration portal. For this portal, Linda Mason (think of her as a project manager for Acme Consulting) is able to onboard new Acme Consulting contractors as she sees fit. Use the credentials below to login as Linda.Mason

| Key | Value
| - | - |
| URL | https://[your-instance-id].mynonemployeeportal.com/contractors/
| Username | Linda.Mason |
| Password | As provided |

Once logged in as Linda, you should be able to see a workflow called `Onboard Contractor`. Click that workflow button and follow the prompts to create a new contractor.

> Keep in mind: the Onboard Contractor workflow invites the contractor to come in and onboard his or herself. This means you need to make sure the email you enter into the first form is an email that you can recieve emails from. This way you will get the email with the registration link for your new contractor

## Demo Script

To go into a little more detail then the `Getting Started` section above, here is the typical demo 'script' that our presales team walks customers through.

### Onboarding a new Contractor

This use case is listed above in brief detail. The main goal of this use case is to enable our customers to easily onboard their non-employees into their environment as efficiently as possible while still having the proper  controls in place from an audit standpoint.

The following steps help you walk thru this use case:

* Navigate to the contractors collaboration portal: https://[your-instance-id].mynonemployeeportal.com/contractors
* Login as `Linda.Mason`
* When the portal dashboard loads, you should be able to see a workflow `Onboard Contractor`. Click this workflow button
* A request form will show up and ask you to fill out this new contractor details. 
* Enter a `First Name`, `Last Name`, and `Email`

> This email value should be a real email address that you have access to. A regsitration link will get sent to this address

> Tip: https://randomuser.me/ is a nice resource to generate randomized user information

* Next, talk about how the Start Date / End Date can be automatically set based on customer requirements. In this case, the start date defaults to the current day and the end date is 90 days from today.
* Then, talk about how the `Vendor` attribute is read-only (meaning this user cannot adjust the vendor). This is because the user is logged into the Acme Consulting portal, so the only non-employees that can be created have to belong to the *Acme Consulting* org.
* Finally, select the `Non Employee Type`. This field does adjust the risk score. If you select, `Consultant` as the non employee type, another dropdown will be displayed asking you to select a project. Choose a project and continue.

> Later on in the flow, a High Risk notification will be shown if a user's risk score is 6 or above.
> * IT Service will have a risk score of `9`
> * Consultant will have a risk score of `7`
> * Staf Aug will have a risk score of `2`

* After the entire form is filled out appropriately, click **Submit** to continue the onboardig process
* At this point an email will be sent to the email address of this new contractor. Pull up that email and click `Get Started` registration link towards the bottom of the email
* The registration link will redirect you to a new page and you will be acting on behalf of that new contractor. Talk about how this new contractor can see the information that Linda Mason entered into the previous form. This new contractor can choose to change his/her first name or last name if something was incorrectly entered.
* The contractor can also see his/her start date and end date, but can no longer change these details.
* The only question this contractor needs to answer is `Are you able to come onsite for verification?`. Click `No` for this question and begin scrolling down the page.

> By selecting `No` on the question mentioned above, the workflow will trigger a digitial Identity Proof for this new contractor. If you don't need to walk through the Identity Proofing step, select `Yes` to skip it as necessary

* Talk through the digital Acceptable Use Policy that the contractor has to accept. Scroll to the bottom of the page and click **Submit**

> By hitting the submit button SecZetta logs when the contractor accepted this policy and what policy was accepted. These details will be shown to approvers as the onboarding process progresses

#### Identify Proofing (if applicable)

* If `No` was selected for the question `Are you able to come onsite for verification?`, then the next page in the workflow should say `Identity Proofing`. Click **Verify My Identity** to begin the process

> When a client uses this module in production, a cell phone number will likely be used and a SMS message will be sent to the contractors phone to perform this digital identity proofing. For demo purposes, this is all done via the browser.

* This should launch our Identity Proofing module and the first question that will be asked is `Which type of ID would you like to use?`. Select **Driver's License** and then Click **Confirm Information**

> Driver's Licnese, Passport, and Other ID are different ID Types we support. There are 6000+ IDs that are supported in over 190 countries

* On the `Document Capture` screen, hit **Start**
* Click **Capture Using Your Phone Camera** and upload the imaged named `male-1-license-front.jpg` or `female-1-license-front.jpg` depending on the gender of your contractor

> These images should have been sent in your demo baseline package. Reach out to Taylor Hook (thook@seczetta.com) if you didnt recieve them.

* Click **Save and Next**
* Click **Capture Using Your Phone Camera** and upload the imaged named `male-2-license-back.jpg` or `female-2-license-back.jpg` depending on the gender of your contractor
* Click **Save and Next**
* Click **Capture Using Your Phone Camera** and upload the imaged named `male-2-license-face.jpg` or `female-2-license-face.jpg` depending on the gender of your contractor
* Click **Save and Next**
* Fill out the **Date of Birth** field
* Scoll down and click **Submit**
* If everything was successfully uploaded a `Success. Your identity has been verified message` should be displayed. Click **Submit** to continue.

#### Continue with Onboarding

* At this point, you have either skipped Identity Proofing or just finished walking through the Identity Proofing module. Either way, a screen listing all of the steps you have walked through so far should be displayed. 
* Now it is time to login to the Lifecycle portion of the product. Using your administrative account navigate to the Lifecycle Dashboard: https://[your-instance-id].mynonemployee.com
* Once logged in, there should be a banner across the top of the dashboard saying `You have requests that need your action`. Click that banner.
* There will be a pending request named `Contractor Registration by Invite`. Click that request to open it up.
* This is the approval for a Contractor thats about to be created. Someone on the customer side will almost certainly have to approve the creation of this contractor before any accounts or access is granted. Scroll down the page describing all of the detail in the approval form.
* At the bottom of the form, there will be three (3) questions that the approver will be required to answer. Answer them however you want, just know that the answers to these questions adjust the risk score of the contractor

> The best way to get the highest risk on this contractor would be to answer the questions `Yes`, `Yes`, `No` from left to right. Below is the breakdown of the risk scores that will be applied
> * If `Will this person be provided equipment?` is answered as `Yes`. An avg risk score of 6.2 will be applied
> * If `Will remote access be required?` is answered as `Yes`. An avg risk score of 7.8 will be applied
> * If `Is company provided training required?` is answered `No` a 5.0 risk score will be applied

* After answering the questions, click **Approve** to continue with the onboarding process
* If the new contractor has a high risk level, a form will show indicating as such. If this form shows click **Submit** to finish off the onboarding process.
* This is the final step in the onboarding process. The new contractor has officially been onboarding and his/her profile should be visible within SecZetta.

### Revalidate an existing profile

On a semi-regular basis SecZetta will send off `Revalidation` requests for non-employees that have been performing work for the client. Typically this is done X number of days after 'hire'. For this use case, we will manually kick of a Revalidation request, just know that this will normally be an automated workflow that would trigger this to occur on specified dates.

To manually kick off a Revalidation follow the steps below:

* Using your administrative account navigate to the Lifecycle Dashboard: https://[your-instance-id].mynonemployee.com
* From the dashboard, open up an **Active** `Person` profile to view their profile information.
* When the profile page loads, you should see a few workflows you can execute on this profile. Begin the revalidation by clicking the **Revalidate** workflow button
* A simple page notification will appear, telling you what you are about to do. Click **Submit** to continue
* Now it is time to login as a Collaborator. Navigate to the contractors collaboration portal: https://[your-instance-id].mynonemployeeportal.com/contractors
* Login as `Linda.Mason`
* Once logged in, there should be a banner across the top of the dashboard saying `You have requests that need your action`. Click that banner.
* There will be a pending request named `Revalidate`. Click that request to open it up.
* This Revalidation request is asking Linda to review the current contractor information and asks for input from Linda about the contractor. For the question: `Is this person still actively engaged?` select `No` to start the termination process

> Feel free to answer in other ways, by selecting `No` this will automatically kick off a termination process. If you select `Yes` additional questions will show asking to validate more information.

* After selecting `No`, Linda's job is complete. However, because a termination now needs to happen, an internal user was sent an approval for this termination
* Using your administrative account navigate to the Lifecycle Dashboard: https://[your-instance-id].mynonemployee.com
* Once logged in, there should be a banner across the top of the dashboard saying `You have requests that need your action`. Click that banner.
* There will be a pending request named `Terminate`. Click that request to open it up.
* Review the information, and click **Approve** below to complete the termination
* Search for this profile that was just revalidated/terminated and you will see that their status has changed to Terminated. From here, an IAM system would take action and disable/delete accounts as necessary

### Terminate a profile

Just as discussed above with revalidations, terminations will likely automatically happen on a scheduled basis based on the end date of the non-employee. For our case, we will manually trigger a termination event to occur.

To manually kick off a Termination follow the steps below:

* Using your administrative account navigate to the Lifecycle Dashboard: https://[your-instance-id].mynonemployee.com
* From the dashboard, open up an **Active** `Person` profile to view their profile information.
* When the profile page loads, you should see a few workflows you can execute on this profile. Begin the revalidation by clicking the **Terminate** workflow button
* A request form page will appear asking you to enter a `Termination Reason`. Add a reason for termination and click **Submit** to continue

> Profile Tags are also able to be set here, if there was a termination for cause and you wanted to set the `Do Not Hire` flag, feel free to do so

* Now an approval is required, because an Administrator initiated this termination request he also gets the approval. Review the information of this soon to be terminated profile and click **Approve** to continue

> This approval step could techcnially have been skipped because the requester is the same user as the approver. This approval can be skpiped by setting `Skippable Approval?` in the workflow step. For demo purposes, this has purposely remained unchecked

* At this point, the termination process is complete and the profile should now have a status of `Terminated`

> If you now pull up this inactive profile, the termination reason should now appear on that profile's page

### Make Collaborator

* Using your administrative account navigate to the Lifecycle Dashboard: https://[your-instance-id].mynonemployee.com
* From the dashboard, open up an **Active** `Person` profile to view their profile information.
* When the profile page loads, you should see a few workflows you can execute on this profile. Begin the revalidation by clicking the **Make Collaborator** workflow button
* A simple page notifying you that this profile will recieve and email asking them to register their collaboration account. After verifying the email click **Submit** to continue

> This email address needs to be an email account you can access. This email will contain the registration request that the profile will need to complete this process

* An email will be sent to the address stored in SecZetta. Look up that email and click the link at the bottom of the email to begin the Collaboration account creation.

> At this point, you are acting as this profile being promoted to Collaborator. In the real world, this would be sent to an external person that would recieve that email and sign up on their own

* Once you've followed the link, you will get presented with a new form asking you set your password. The username should have defaulted to `First Name`.`Last Name`. Set your password and click **Submit** to create the Collaboration account
* Now this account, should be able to log into the `/contractors` portal. Navigate to the contractors collaboration portal: https://[your-instance-id].mynonemployeeportal.com/contractors
* Login as using this new username and password to verify this new profile has a new Collaboration account

### Add a new Vendor

Sometimes, Clients will have an existing list of vendors and/or an entire system to manage Vendors (VMS). SecZetta will connect to that list of system to pull Vendor information into its repository. This next use case just shows the ability for SecZetta to handle the onboarding of new Vendor entities. 

* Using your administrative account navigate to the Lifecycle Dashboard: https://[your-instance-id].mynonemployee.com
* When the dashboard loads, you should be able to see a workflow `New Third Party Vendor`. Click this workflow button
* Fill out the required Vendor information and click **Submit** to continue

> An approval will be sent out to various groups (configurable per workflow). The Admin should also get this approvals so it should should just automatically show after you've clicked Submit.

* Review the Vendor information and click **Approve** to complete this request

### Add a new Project

Projects was another profile type that is built into the demo baseline. This could be any other type of object your client wants to manage. Projects are a good example because it is easy to wrap your head around the relationships between people and projects. These next few steps show you how to quickly create a new project profile

* Using your administrative account navigate to the Lifecycle Dashboard: https://[your-instance-id].mynonemployee.com
* When the dashboard loads, you should be able to see a workflow `New Project`. Click this workflow button
* Fill out the required Project information and click **Submit** to continue.
* Success. A project was created

## Workflows

In SecZetta there are two (2) 'modules' that you will be working with throughout a typical deployment: Lifecycle (previously known as NEProfile) and Collaboration (previously known as NEAccess). Each module has its own workflows that can be created/updated.

Workflows themselves is the mechanism where SecZetta can interact with the various profile types in the system. These workflows come in a few different variations, but the 3 most common workflow types are Create, Update, and Portal Registration. Create workflows will show up on the dashboard of any user who has access to run the workflow. Update workflows will show up when viewing a particular profile for any user who has access to run the workflow as well. Portal Registration workflows can be called on the Collaboration portals themselves (via Self-service) or can be triggered via a Registration Invitation workflow step in a Create/Update workflow.

The table below lists the functional workflows and the module where you will find it.

| Workflow Name                    | Description | Module | Type
|----------------------------------|-------------|--------|-------|
| Integration - Create IDN Account | Used for IAM integrations. Called as a subworkflow inside the Contractor Registration workflow(s) | Lifecycle | Create |
|Invite Contractor | Used in the Lifecycle module to allow Z Corp users to invite a new contractor to be onboarded (Calls `Contractor Registration by Invite` via Registration Invitation action) | Lifecycle | Create |
| New Project | Onboards a new project profile type | Lifecycle | Create |
| New Third Party Vendor | Onboards a new vendor profile type | Lifecycle | Create |
| Onboard Contractor | Used in the Collaboration module to allow external third parties to onboard contractors into the Z Corp environment (Calls `Contractor Registration by Invite` via Registration Invitation action) | Lifecycle | Create
| Contractor Registration | A self-service Registration workflow that is used to onboard the Contractor. This workflow will show up on the  `/contractors` portal login page | Collaboration | Portal Registration |
| Contractor Registration by Invite | A very similar workflow to Contractor Registration. The only difference here is the Contractor will be presented with a form that has his/her `first_name`, `last_name`, and `email` attributes filled out by the person who invited them. | Collaboration | Portal Registration
| Vendor Admin Registration | This registration workflow creates new Collaborators to the `/contractors` portal. Called by the `Make Collaborator` update workflow | Collaboration | Portal Registration
| Make Collaborator | Called on People profile types to create a Collaborator account. (Calls the `Vendor Admin Registration` workflow) | Collaboration | Portal Registration
| Revalidate | Sends off a revalidation item to the person's sponsor | Lifecycle | Update
| Terminate | Changes the status of a profile to terminated | Lifecycle | Update
| Troubeshoot Data | Disabled workflow that was used to check out data attributes as they progress thru certain workflow actions | Lifecycle | Update
| Login | Very basic workflow that allows Collaborators to login using their username and password | Collaboration | Login

## Attributes

Attributes in SecZetta are not tied to a particular profile type and can be used acrossed profile types. The attribute design is certainly something that needs to be discussed and agreed upon before building out the product. In the demo baseline there *relatively* basic profile types that we are working with so the attribute design isn't as complex. However, this can get much more complex as you start seeing other real world scenarios.

There is a table below that lists the more important attributes of the demo baseline. This is not an exhaustive list, you can find that in your attributes page in the admin console (**Templates** -> **Attributes**).

|UID | Label | Description | Profile Types | Example Values
|-|-|-|-|-|
| profile_uid_ne_attribute | Profile UID | Unique ID for profile | People | SZ000011
| people_vendor | Vendor | Stores the vendor relationship | People | Acme Consulting
| non_employee_type | Non Employee Type | Dropdown to determine what type of person this non-employee is | People | IT Service
| sponsor | Sponsor | People, Projects, Vendor | Sheila Andersen
| profile_flags | Profile Flag(s) | Allows you to flag a particular profile | People | Do Not Hire
| first_name | First Name | | People | Sheila
| last_name | Last Name | | People | Andersen
| email | Email | | People | Shila.Andersen@acme.com
| onboard_source | Onboard Source | Where did this profile get onboarded | People | Invite
| invitation_status | Invitation Status | Did the person accept the invite yet? | People | Accepted
| start_date | Start Date | When the non-employee starts work | People | 01/01/2001
| end_date | End Date | When the non-employee is scheduled to end work | People | 01/01/2001
| termination_date | Termination Date | When the non-employee officially was terminated | People | 01/01/2001
| idp_status | IDProofing Status | Status of the IDProofing step (if applicable) | People | Passed
| idp_requested_verification_date | Requested Verification Date | When was IDProofing requested (if applicable) | People | 01/01/2001
| idp_date_proofed | Date Proofed | Date the person actually proofed (if applicable) | People | 01/01/2021
| signed_acceptance_policy | Signed Policy | Which poilcy did they sign | People | Acceptance Policy v1
| policy_signed_date | Policy Signed Date | When did they sign the policy | People | 01/01/2021
| Signed Policy | signed_policy_name | Flag that indicates if they signed the policy | People | Yes

## Permissions (User Roles)

User Roles are important because they are what give the proper permissions to your user(s). For our demo baseline, there are only a few that are in use as of today. There are a couple more user roles that will be used for more use cases as we continue to build onto this baseline.

User roles are auto assigned based on group membership that would come thru in a SAML assersion. This causes some minor problems when it comes to demo environments, because we cant define local users (yet) to have the proper permissions for certain activities.  

For now, the user roles listed below are the only ones that need to be understood.

User Role | Description | Lifcycle / Portal?
| - | - | - |
Admin | Allows administrative access to the tool. In the demo baseline, these administrators will recieve any approvals that are necessary | Lifecycle
Sponsor | Controls a contributor dropdown box, so people can choose people in this userrole as a Sponsor for a particular profile | Lifecycle
Collaborators | Gives users the ability to manage a vendor | Lifecycle
Acme Consulting Admins | Collaborators specifically for the Acme Consluting Vendor and people profiles | Portal


## Helpful Links

See the links below for additional resources

* [Partner Portal](https://seczetta.sharepoint.com/sites/PartnerEnablement)
* [User Guide](https://seczetta.sharepoint.com/documentation/SitePages/Home.aspx?RootFolder=%2Fdocumentation%2FShared%20Documents%2F1%5FProduct%20Documentation%2Fv4%2E5&FolderCTID=0x01200012980FD71E0362419D9F4668088AE99A&View=%7B0821AEE9%2D50B6%2D4D2B%2DA0BC%2D044EAC0915BA%7D)
* [Admin Guide](https://seczetta.sharepoint.com/documentation/SitePages/Home.aspx?RootFolder=%2Fdocumentation%2FShared%20Documents%2F1%5FProduct%20Documentation%2Fv4%2E5&FolderCTID=0x01200012980FD71E0362419D9F4668088AE99A&View=%7B0821AEE9%2D50B6%2D4D2B%2DA0BC%2D044EAC0915BA%7D)