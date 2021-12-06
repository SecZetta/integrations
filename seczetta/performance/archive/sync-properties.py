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

API_BASE = "https://marriottperformancedev.nonemployee.com/api"
API_KEY = "18bae8c5f1944a71a502721ba460b18d"
PEOPLE_PROFILE_TYPE_ID = "1bd99a83-57e1-4e3c-bbb0-861b4700cff6"
USER_GARBAGE_CAN_USER = "2d595872-7a0a-40c6-a519-3013d000bcb2"
PROFILE_TYPE_ID_COMPANIES = "57ad1a76-9bbe-48d3-825e-4a967ab3f372"
PROFILE_TYPE_ID_PROPERTIES = "47e9fe1b-003f-4be6-90aa-f852aadb5628"
PROFILE_TYPE_ID_NON_ASSOCIATES = "f6eca1ce-db43-41cf-b32a-806419ec9595"
ATTRIBUTE_ID_COMPANY_NAME = "a7a9abc0-8e24-4c58-a0c9-6d7fb3bc6d69"
ATTRIBUTE_ID_PROPERTY_NAME = "6d5a37ba-d365-4ce6-aba6-4849a800c08d"
ATTRIBUTE_ID_PROPERTY_MANAGEMENT_COMPANY = "1a92bea4-78b7-4e9e-957b-79ab9665ada3"
ATTRIBUTE_ID_PROPERTY_OWNER_COMPANY = "72031d62-4203-4d60-86d2-5982aaa675e4"
ATTRIBUTE_ID_PROPERTY_FRANCHISEE_COMPANY = "0d2641c7-cf2d-4cd0-8ea5-d19b465b87f0"
ATTRIBUTE_ID_NON_ASSOCIATE_PROPERTY = "aa29a165-f767-4ff3-8f74-d296341e0bde"

USER_ID_NEPROFILE0 = "8fb88141-4a4e-48b0-98fc-3d6f257394b0"

WORKFLOW_ID_CREATE_PROPERTY = "ada79c48-6694-4440-9dfb-f47d4f1c045a"
WORKFLOW_ID_CREATE_PROPERTY = "ada79c48-6694-4440-9dfb-f47d4f1c045a"
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


def processFile(filename):
    fileDict = {}
    lines = 0
    with open(filename) as f:
        for line in f:
            lines+=1
    return lines

def read():
    csv_cached = "/Users/taylorhook/Documents/SecZetta/Development/integrations/seczetta/performance/data/cached/SZ_Properties-fixed.csv"
    csv_new = "/Users/taylorhook/Documents/SecZetta/Development/integrations/seczetta/performance/data/SZ_Properties-new.csv"
    dfCached = pd.read_csv(csv_cached)
    dfNew = pd.read_csv(csv_new)
    dfCached.set_index("prop_id", inplace=True)
    dfNew.set_index("prop_id", inplace=True)
    #print(df)

    diffs = pd.concat([dfCached,dfNew]).drop_duplicates(keep=False)

    print(diffs)

def process_gl():
    start_time = time.time()
    gl_dtype = {
        'first_column': 'str', 
        'second_column': 'str',
        'Legacy_Division':'str',
        'Legacy_Unit': 'str',
        'Legacy_Department': 'str',
        'Division': 'str',
        'Op_Unit': 'str',
        'DEPTID': 'str',
        'Effective_Date': 'str'
    }
    csv_cached = "/Users/taylorhook/Documents/SecZetta/Development/integrations/seczetta/performance/data/cached/GL_DEPT_L1_to_L3_20190920.DAT"
    csv_new = "/Users/taylorhook/Documents/SecZetta/Development/integrations/seczetta/performance/data/GL_DEPT_L1_to_L3_20190920.DAT"
    dfCached = pd.read_csv(csv_cached, sep="|", dtype=gl_dtype)
    dfNew = pd.read_csv(csv_new, sep="|", dtype=gl_dtype)

    
    dfCached.set_index("Legacy_Division~Legacy_Unit~Legacy_Department~Effective_Date", inplace=True)
    dfNew.set_index("Legacy_Division~Legacy_Unit~Legacy_Department~Effective_Date", inplace=True)

    diffs = pd.concat([dfNew,dfCached,]).drop_duplicates(keep=False)

    creates = []
    updates = []
    deletes = []

    for index, row in diffs.iterrows():
        #Get Creates
        if index in dfNew and index not in dfCached:
            #creates
            creates.append(dfNew.loc[index])
        elif index in dfNew and index in dfCached:
            #updates
            updates.append(dfNew.loc[index])
        elif index not in dfNew and index in dfCached:
            #deletes
            dfNew.loc[index]
        else:
            log.warning("Something file difference didnt match an create, update, or delete")
        
    print("Creates ", creates)
    print("Updates ", updates)
    print("Deletes ", deletes)

    print(time.time() - start_time)


#lines = processFile("/Users/taylorhook/Documents/SecZetta/Development/integrations/seczetta/performance/data/cached/SZ_Properties.csv")
#log.info("Processed %s lines", lines)


#read()
#process_gl()

response = launchCreateWorkflow(WORKFLOW_ID_CREATE_PROPERTY, USER_ID_NEPROFILE0, "NeprofileUser", {"property_name" : "My Property"})
print(response.json())