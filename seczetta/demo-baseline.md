# SecZetta - Demo Baseline

## Introduction

This baseline is what our presales team uses as a *standard* demo we would give to our clients. This baseline includes three (3) different profiles types: People, Vendors, Projects. The use case is the typcial contractor onboarding flow that our customers utlize the tool to solve.

This demo baseline will give you a good insight into how to configure SecZetta in order to solve some of your customer's non-employee problems. The primary purpose of this documentation is to outline what is built and how to make adjustments if required. There are two Organizations that will be mentioned throughout the documentation and in the tool itself.

* **Z Corp:** This is the organization that is using SecZetta to manage their non employees.
* **Acme Consulting:** This is the third party organization that is doing work for Z Corp.

## Workflows 

In SecZetta there are two (2) 'modules' that you will be working with throughout a typical deployment: Lifecycle (previously known as NEProfile) and Collaboration (previously known as NEAccess). Each module has its own workflows that can be created/updated. The table below lists the functional workflows and the module where you will find it

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