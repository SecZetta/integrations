# Liquid Reference Guide

## Introduction

Liquid is used inside SecZetta to help display profile attributes in `Pages`,`Notifications`, and `Rest API Actions` . The liquid syntax allows you to easily access specific data attributes based on the current context. Currently the three SecZetta objects listed above are where liquid is used. The team is always expanding the use of liquid throughout the product, so upcoming versions could have this being used in other places as well.

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
* `workflow` - used in notification to get the current workflow this email notification is being called from (`{{workflow.name}}` is primarily used)

### Tags 

Tags create the logic and control flow for templates. The curly brace percentage delimiters `{%` and `%}` and the text that they surround do not produce any visible output when the template is rendered. This lets you assign variables and create conditions or loops without showing any of the Liquid logic on the page.

These tags are very useful in a SecZetta context to manipulate data before showing it or sending it to an external system.

Tags can be categorized into four various types:
* Control flow
* Iteration
* Template
* Variable assignment

#### Control Flow
Control flow tags create conditions that decide whether blocks of Liquid code get executed.

##### if

Executes a block of code only if a certain condition is true.

###### Input

```
{% if product.title == "Awesome Shoes" %}
  These shoes are awesome!
{% endif %}
```
###### Output
```
These shoes are awesome!
```

unless
The opposite of if – executes a block of code only if a certain condition is not met.

Input

{% unless product.title == "Awesome Shoes" %}
  These shoes are not awesome.
{% endunless %}
Output

These shoes are not awesome.
This would be the equivalent of doing the following:

{% if product.title != "Awesome Shoes" %}
  These shoes are not awesome.
{% endif %}
elsif / else
Adds more conditions within an if or unless block.

Input

<!-- If customer.name = "anonymous" -->
{% if customer.name == "kevin" %}
  Hey Kevin!
{% elsif customer.name == "anonymous" %}
  Hey Anonymous!
{% else %}
  Hi Stranger!
{% endif %}
Output

Hey Anonymous!
case/when
Creates a switch statement to execute a particular block of code when a variable has a specified value. case initializes the switch statement, and when statements define the various conditions.

An optional else statement at the end of the case provides code to execute if none of the conditions are met.

Input

{% assign handle = "cake" %}
{% case handle %}
  {% when "cake" %}
     This is a cake
  {% when "cookie", "biscuit" %}
     This is a cookie
  {% else %}
     This is not a cake nor a cookie
{% endcase %}
Output

This is a cake

