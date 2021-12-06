from pandas.core.dtypes.missing import isnull
import requests
from random import randrange
import time
from os.path import exists
import json
import logging as log
import pandas as pd
import time




log.basicConfig(level=log.INFO)


from requests.api import get

API_BASE = "https://requests.myseczetta.com/api"
API_KEY = "e56628ef714648b3b76347c8df2c4d82"

USER_ID_SARAH = "6b335979-38a0-4fca-a3fb-e59bea676e37"
USER_ID_NEPROFILE0 = "8fb88141-4a4e-48b0-98fc-3d6f257394b0"
WORKFLOW_ID_CREATE_PARTNER_RESOURCE = "f0939bdc-ca91-4d28-9e66-888fc9958ecb"
WORKFLOW_STEP = "52c08dff-271f-423a-9326-fc24d1f7b8e7"
INCREMENTAL_ID = 1


#########################################################################################################
# Name: Send API Request
# Purpose: 
#   Processes Generic API Requests. Mostly used to call the SecZetta API
#########################################################################################################
def sendAPIRequest(verb, url, data):
    log.info("Entering sendAPIRequest %s %s", verb, url)

    verb = verb.upper()
    url = API_BASE + url

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token='+API_KEY,
        'Accept': 'application/json'
    }

    log.info("New URL: " + url)

    response = ""
    if(verb == "GET"):
        response = requests.get(url, headers=headers, json =data)

    if(verb == "POST"):
        response = requests.post(url, headers=headers, json = data)

    if(verb == "PATCH"):
        response = requests.patch(url, headers=headers, json = data)

    return response

def launchCreateWorkflow(workflow_id, requester_id, requester_type = "NeProfileUser", attributes = {}):

    data = {
        "workflow_session": {
            "workflow_id": workflow_id,
            "requester_id": requester_id,
            "requester_type": requester_type,
            "attributes": attributes
        }
    }

    log.info(data)

    return sendAPIRequest("POST", "/workflow_sessions", data)


#########################################################################################################
# Name: Send API Request
# Purpose: 
#   Uses DataFrames to parse the CSV data quickly. Loops thru the CSV provided and lanches a workflow for
#   each record
#########################################################################################################
def processFile(filename):
    df = pd.read_csv(filename)
    i = 1
    for index, row in df.iterrows():
        first_name = row['personal_first_name']
        last_name = row['personal_last_name']
        email = row['partner_email']
        org = row['partners_organization']
        org_type = row['partner_type']
        sharepoint_date = row['partner_sharepoint_invite_date']
        sharepoint_source = row['partner_sharepoint_invite_source']

        if isnull(sharepoint_date):
            print("No Sharepoint DATE!")
            sharepoint_date = None
        
        if isnull(sharepoint_source):
            print("No Sharepoint source!")
            sharepoint_source = None


        
        sz_dict = {
            "personal_first_name": first_name,
            "personal_last_name": last_name,
            "partner_email": email,
            "partners_organization": org,
            "partner_type": org_type,
            "partner_sharepoint_invite_date": sharepoint_date,
            "partner_sharepoint_invite_source": USER_ID_SARAH
        }
        
        response = launchCreateWorkflow(WORKFLOW_ID_CREATE_PARTNER_RESOURCE, USER_ID_SARAH, "NeprofileUser", sz_dict)
        if response.status_code != 400:
            print(response.json())
        else:
            print("Error Occrred!")
            print(response.json())
        i = i+1
        print("Done with " + str(i))

    return "Success!"

#processFile("new_partners.csv")