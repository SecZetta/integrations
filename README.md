# SecZetta Integrations 

## Purpose

The purpose of this repository is to fully document what it takes to integrate with SecZetta's partner network.

Some of the integrations will be build inside of SecZetta. Some will require external scripts to be accomplished. The documentation and subsequent configuration files stored here will be used by our customers and partners to deploy these integrations within the *SecZetta Identity Suite*. 

## Getting Started

In order to build out any type of integration listed herein, how the various tools commuicate will be a top priority. In most, SecZetta will use one of three ways to communiate:

* External Party uses SecZetta's API endpoint: `<seczetta-tenant-name>.mynonemployee.com/api/<endpoint>`
  * Click [here](https://seczetta.nonemployee.com/api/v1) for API Documentation
* SecZetta uses REST API Action within its own workflows
* An external script runs in the customer's network to pull and push data to and from SecZetta

## Using SecZetta's API


