# Liquid Reference Guide

## Introduction

Liquid is used inside SecZetta to help display profile attributes in pages/emails/workflows. The liquid syntax allows you to easily access specific data attributes based on the current context

Liquid accomplishes this by using a combination of objects, tags, and filters to display, check and maniuplate data

### Objects

The basic Liquid syntax uses the `{{ }}` syntax. For SecZetta, the majority of the time you will use something like `{{ attribute.first_name }}`. This would return the value of the first_name attribute of the current request or profile.

This syntax can be used in Workflow pages with any component in the `Text` collection of a workflow page. This includes:

* Large / Med / Small Headers
* Form Headers
* Paragraphs
* HTML

There are a few different types of liquid type objects that you will see within the SecZetta solution. The list below is ranked from most used to least used:

* `attribute` - this object will be the primary way you will display data about a profile on a page or notification
* `profile` - this object will be used to update the profile pages of a profile type. *Note: `attribute` will **NOT** work on profile pages*
* `request` - used in notifications to get the actual request object itself. Attributes lke created_at,  status, current_action, and coments are used
* `requester` - used in notifications to get current requester. Attributes like name, email, title, and login are available
* `approver` - used in notifications to get the approver (if any) that has made a decision. Approver is very similar to requester so attributes like name, email, title, and login are available *(TODO: check to see what happens if multiple approval steps are in a workflow)*
* `workflow` - used in notification to get the current workflow this email notification is being called from ({{workflow.name}} is primarily used)