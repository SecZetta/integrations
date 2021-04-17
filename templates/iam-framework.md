# IAM Integration

## Getting Started

At the highest of levels, SecZetta can be considered your authoritative source for all non-employee user types. This includes but is not limited to: Contractors, Consultants, 3rd party vendors, Students, Alumni, Doctors, Affiliates and the list can go on and on. SecZetta is **not** a provisioning solution and it relys on its top Identity partners to handle this for our joint customers. Because of this, SecZetta has built certified integrations with many of the top Identity and Access Management (IAM) tools in the market. This guide is not going to go into specifics about particular IAM vendors, but rather discuss the best practices approach on how we integrate with any and all IAM systems.

SecZetta has a robust workflow and collaboration engine that allows our customers to automate complex business processes without the use of complex code. Regardless, at the end of the day SecZetta will be managing various types of `Profile Types`. These Profile Types can be any type of object that a customer may need to manage. The primary ones that an IAM tool will care about is the `People` profile type and potentially the `Assignments` profile type. These profile types will be discussed in detail below. Each profile type will have many different types of profiles and these profiles are going to be what your IAM system cares most about.

There are *primarily* 2 ways our customers integrate with their IAM solutions depending on the capabilities of the IAM tool. The rest of this guide will discuss and expand upon these 2 integration approaches.

### 1. IAM initated data aggregation

This integration is initiated from the IAM system itself. These solutions sometimes call this data aggregations, data collection, or something similar. All of your IAM tools will have some sort of connector framework that will allow data to flow from an external place into the IAM system itself.

Within this integration type there is also 2 ways to go about it. There is a flat file based integration and there is API based integration.

#### Flat File Integration

For this integration the IAM tool simply looks for a file with a specific format in a specific location and pulls all data into the IAM solutions internal database. This integration 'sub-type' is the easiest way to integrate your IAM system with SecZetta.

Common type of file formats are CSV, JSON, and maybe something like XML. CSV being the overwellmingly most popular of the three. Every IAM solution will be able to handle this type of integration. We will assume CSV for the remainder of this documentation

The data in this CSV file will contain all the relavant Identity data to allow the IAM system to properly manage the lifecycle of that user. Things like *firstname*, *lastname*, status, *start date*, *end date* and much, much more will be included in this file.

##### Example CSV (in table form)

| profile_uid | first_name | last_name | status     | start_date |  end_date  |termination_date|
|-------------|------------|-----------|------------|------------|------------|----------------|
| 00000456    | Martha     | Walker    | Active     | 01/01/2001 | 01/01/2030 |                |
| 00000457    | Felicia    | Lucas     | Terminated | 01/02/2001 | 01/01/2020 | 01/01/2020     |
| 00000458    | Brianna    | Bennett   | Active     | 01/01/2001 | 01/01/2030 |                |
| 00000459    | Adrian     | Ryan      | Active     | 01/01/2001 | 01/01/2030 |                |

> Note: A production CSV will have many more fields compared to the example above


#### API Integration

This integration is a much more modern type of integration. In this case, the IAM system has to have a generic REST API connector (*sometimes referred to as a Web Services connector*). SecZetta has a robust API framework that allows IAM systems to easily pull any and all profile data from the SecZetta solution.

### 2. SecZetta-initiated integration

In this type of integration, SecZetta will trigger the updates to the IAM system via RESTful api call. The obvious pre-requisite is that the IAM system has an API framework that is excessible to SecZetta. Knowing that SecZetta is a SaaS solution running in the public cloud this type of integration could be a potential challange for any of those IAM systems that are running on-prem behind the customer's firewall.

More often than not, this type of integration is only really used when the IAM system in question is also a SaaS solution running in the public cloud. This way firewalls are not an issue and everything can commuicate securely without having to poke holes in a customer's  firewall.
