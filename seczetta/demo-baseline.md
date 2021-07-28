# SecZetta - Demo Baseline

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

The easiest way to being to onboard new people is by using the Contractors collaboration portal. For this portal, Linda Mason (think of her as a project manager for Acme Consulting) is able to onboard new Acme Consulting contractors as she sees fit. Use the credentials below to login as Linda.Mason

| Key | Value 
| - | - |
| URL | https://(your-instance-id).mynonemployeeportal.com/contractors/
| Username | Linda.Mason |
| Password | S3cZ3tta!

Once logged in as Linda, you should be able to see a workflow called `Onboard Contractor`. Click that workflow button and follow the prompts to create a new contractor.

> Keep in mind: the Onboard Contractor workflow invites the contractor to come in and onboard his or herself. This means you need to make sure the email you enter into the first form is an email that you can recieve emails from. This way you will get the email with the registration link for your new contractor

## Demo Sript

To go into a little more detail then the `Getting Started` section above, here is the typical demo 'script' that our presales team walks customers through.

### Onboarding a new Contractor

#### Identity Proofing

### Revalidate an existing profile

### Terminate a profile

### Make a Vendor Admin

### Add a new Vendor

### Add a new Project

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
| Vendor Admin Registration | This registration workflow creates new Collaborators to the `/contractors` portal. Called by the `Make Vendor Admin` update workflow | Collaboration | Portal Registration
| Make Vendor Admin | Called on People profile types to create a Collaborator account. (Calls the `Vendor Admin Registration` workflow) | Collaboration | Portal Registration
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
Admin | Allows administrative access to the tool | Lifecycle
Sponsor | Controls a contributor dropdown box, so people can choose people in this userrole as a Sponsor for a particular profile | Lifecycle
Vendor Admin | Gives users the ability to manage a vendor | Lifecycle
Acme Consulting Admins | Vendor Admins specifically for the Acme Consluting Vendor and people profiles | Portal

