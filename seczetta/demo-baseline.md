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
| URL | https://[your-instance-id].mynonemployeeportal.com/contractors/
| Username | Linda.Mason |
| Password | SecZetta1!

Once logged in as Linda, you should be able to see a workflow called `Onboard Contractor`. Click that workflow button and follow the prompts to create a new contractor.

> Keep in mind: the Onboard Contractor workflow invites the contractor to come in and onboard his or herself. This means you need to make sure the email you enter into the first form is an email that you can recieve emails from. This way you will get the email with the registration link for your new contractor

## Demo Script

To go into a little more detail then the `Getting Started` section above, here is the typical demo 'script' that our presales team walks customers through.

### Onboarding a new Contractor

This use case is listed above in brief detail. The main goal of this use case is to enable our customers to easily onboard their non-employees into their environment as efficiently as possible while still having the proper  controls in place from an audit standpoint.

The following steps help you walk thru this use case:

* Navigate to the contractors collaboration portal: https://[your-instance-id].mynonemployeeportal.com/contractors
* Login as `Linda.Mason` with password `SecZetta1!`
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

Duis tortor mauris, sollicitudin eu arcu ut, tristique venenatis arcu. Curabitur dapibus sed ex non venenatis. Praesent nec commodo elit. Etiam a tincidunt tellus, vitae tristique turpis. Praesent quam erat, fringilla viverra quam vel, semper sollicitudin arcu. Aenean ullamcorper convallis purus. Nunc faucibus enim aliquam cursus tempus. Quisque tincidunt, leo ac aliquam porta, odio est efficitur dui, a ultricies nulla tortor eu lacus. Nulla metus lacus, maximus id pretium in, imperdiet eu est. Curabitur rutrum felis et posuere varius. Quisque lacinia purus mattis suscipit pellentesque. Vivamus tincidunt nunc in dignissim interdum.

### Terminate a profile

Nullam ut nisl at erat dapibus pretium ac fringilla tortor. Phasellus ullamcorper, eros a rhoncus placerat, ex tellus facilisis mauris, sit amet egestas nisi lectus ullamcorper ante. Fusce aliquam porta nisl in sagittis. Proin dapibus faucibus semper. Nunc non lorem non odio vehicula lacinia. Donec venenatis ipsum ac vulputate auctor. Curabitur quis leo faucibus massa gravida hendrerit eget id libero. Vivamus sit amet maximus nulla, eu eleifend odio. Cras mattis ex eget sem venenatis gravida. Phasellus pharetra, ligula in laoreet efficitur, enim purus placerat purus, nec aliquet odio lectus at sem. Vivamus eget aliquam ligula. Nullam augue sem, aliquam nec pharetra vitae, elementum in quam. Cras vitae augue nunc. Nulla et semper augue, luctus laoreet ipsum.

### Make a Vendor Admin

Nunc elementum risus a felis pretium aliquam. Nullam condimentum cursus purus ac tincidunt. Morbi vestibulum lacus a neque vulputate volutpat. Nullam tempus nec elit ut ullamcorper. Nullam non pellentesque erat. Quisque purus sapien, malesuada non efficitur at, facilisis sed lorem. Fusce ut odio convallis, egestas dui at, mattis turpis. Donec tempor nulla eu tincidunt volutpat. Etiam elementum elit a vulputate euismod. Vestibulum non pretium leo, et vehicula ante.

### Add a new Vendor

Sed egestas volutpat rutrum. Suspendisse cursus, velit id lacinia egestas, eros tellus egestas quam, vel vestibulum ipsum est vel ipsum. Mauris urna nibh, pharetra et eros in, sagittis efficitur sem. Maecenas vel ornare mauris. Suspendisse aliquam volutpat risus. Integer tempus interdum consequat. In hac habitasse platea dictumst. Pellentesque pulvinar risus non venenatis condimentum.

Nulla facilisi. Suspendisse dapibus sapien eu nisi pharetra fermentum. Phasellus fermentum tortor massa, id pharetra enim luctus in. Nulla bibendum, dolor at lobortis fringilla, purus nulla posuere dui, ac auctor nulla felis id augue. Phasellus at commodo velit. Duis non justo cursus, ultricies erat at, eleifend enim. Mauris lobortis leo eu lacus sodales, et pharetra urna tempor. Mauris dolor ipsum, vestibulum nec porttitor in, egestas vitae lectus. Maecenas vestibulum erat libero, non laoreet arcu gravida sed. Ut rutrum vestibulum nibh. Nullam orci quam, fringilla et aliquet eu, auctor in sem. Curabitur vehicula, libero eget molestie sodales, mi elit finibus tellus, id luctus risus est quis tellus. Morbi facilisis vulputate neque, nec pretium nibh fringilla vitae. Pellentesque ullamcorper ante eget maximus egestas.

### Add a new Project

Morbi finibus dui in libero egestas, nec varius nibh porta. Vivamus libero justo, rutrum sit amet fringilla ac, semper et mauris. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quis mi vel arcu tincidunt rhoncus eget id nunc. Quisque porttitor bibendum eleifend. Quisque id mi at dui varius mollis. Etiam convallis dolor et dignissim venenatis. In id velit metus. Donec laoreet eu quam sit amet commodo. Etiam lacus dui, pellentesque quis viverra vel, imperdiet vitae elit.

Fusce ex lacus, efficitur id sagittis in, consequat eget nunc. Sed sagittis purus sed est maximus tincidunt quis ac magna. Nam iaculis scelerisque elit. Proin tincidunt interdum velit a consectetur. Proin elementum erat a est semper, vitae mattis risus commodo. Maecenas lacinia non eros sed vehicula. Suspendisse malesuada est at tempus suscipit. Vivamus id scelerisque eros. Duis dui sem, vestibulum eu dignissim id, sodales non elit. Integer pharetra eu nunc nec fermentum. In hac habitasse platea dictumst. Ut gravida est quis lectus aliquam consequat. Maecenas tempor nec metus et tempus.

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
Admin | Allows administrative access to the tool. In the demo baseline, these administrators will recieve any approvals that are necessary | Lifecycle
Sponsor | Controls a contributor dropdown box, so people can choose people in this userrole as a Sponsor for a particular profile | Lifecycle
Vendor Admin | Gives users the ability to manage a vendor | Lifecycle
Acme Consulting Admins | Vendor Admins specifically for the Acme Consluting Vendor and people profiles | Portal

