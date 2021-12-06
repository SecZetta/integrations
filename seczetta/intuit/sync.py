from os import stat
import requests
from random import randrange
from os.path import exists
import logging as log
import time
import csv

log.basicConfig(level=log.INFO)


from requests.api import get

# Base Config
API_BASE = "https://intuitpoc.mynonemployee.com/api"
API_KEY = "135f86942fdc493dbbca5f6d6e596d7a"
OKTA_API_KEY = "005to33fGzwAIWmvLqxKHjNE0Qey0POaeib3MxZOnV"

OKTA_USER_CACHE_FILE_PATH = "okta.cache"
OKTA_CACHE_LOADED = False
OKTA_CACHE = {}

COMPANY_ID_CREDIT_KARMA = "f28d1db0-e35e-4910-85f8-3d7483d06a97"

#########################################################################################################
# Name: Send API Request
# Purpose: 
#   Processes SecZetta API Requests. This appends the appropriate SecZetta Headers to call the API
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

#########################################################################################################
# Name: Send Okta API Request
# Purpose: 
#   Processes Okta API Requests. This appends the appropriate Okta Headers to call the API
#########################################################################################################
def sendOktaAPIRequest(verb, url, data):
    log.info("Entering sendAPIRequest %s %s", verb, url)

    verb = verb.upper()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'SSWS '+OKTA_API_KEY,
        'Accept': 'application/json'
    }
    
    response = ""
    if(verb == "GET"):
        response = requests.get(url, headers=headers, json =data)

    if(verb == "POST"):
        response = requests.post(url, headers=headers, json = data)

    if(verb == "PATCH"):
        response = requests.patch(url, headers=headers, json = data)

    return response

#########################################################################################################
# Name: Get Okta Users By Group
# Parameters:
#   group_id: The id of the group that contains the users you want to pull into SecZetta 
# Purpose: 
#   This will grab all users of a specific group and return them in JSON format ready to be pushed to 
#   SecZetta
# Returns:
#   Array of SecZetta Users ready to be created/updated
#########################################################################################################
def getOktaUsersByGroup(group_id):
    users = []
    okta_response = sendOktaAPIRequest("GET","https://creditkarmadev.oktapreview.com/api/v1/groups/"+group_id+"/users",{})
    if okta_response.status_code == 200:
        for user in okta_response.json():
            sz_user = processUser(user)
            if sz_user != None:
                users.append(sz_user)
    else:
        log.error("Okta API Call Failed. Error Code: %s", okta_response.status_code)

    return users

#########################################################################################################
# Name: Process User
# Parameters:
#   user: The JSON user object from Okta
# Purpose: 
#   This function is called by 'getOktaUsersbyGroup' to process the JSON user object to verify that its
#   a valid user that should be pulled into SecZetta. 
# Returns:
#   A SecZetta user that is ready to be created/updated in SecZetta.
#########################################################################################################
def processUser(user):
    status = user["status"]
    login = user["profile"]["login"]

    if status != "ACTIVE":
        log.info("User: %s is not Active. Skipping!", login)
        return None

    user_json = {
        "profile": {
            "profile_type_id": "11116b36-a0a2-4576-989e-7fddc3c9f63e",
            "status": 1,
            "attributes": {
                "first_name": user["profile"]["firstName"],
                "last_name": user["profile"]["lastName"],
                "email": user["profile"]["email"],
                "okta_id_ne_attribute": user["id"],
                "okta_provisioning_status": user["status"],
                "people_company": COMPANY_ID_CREDIT_KARMA,
                "okta_created_date": user["created"],
                "okta_activated_date": user["activated"],
                "okta_status_change_date": user["statusChanged"],
                "okta_last_login": user["lastLogin"],
                "okta_last_updated_date": user["lastUpdated"]
            }
        }
    }


            # "service_account": false,
            # "Vertical": "Overhead",
            # "ckCompany": "Credit Karma, Inc.",
            # "lastName": "Johnson",
            # "zipCode": "94607-4192",
            # "city": "Oakland",
            # "displayName": "Tim Johnson",
            # "title": "IT Client Engineer II",
            # "login": "tim.johnson@ckcorptest.com",
            # "employeeNumber": "100711",
            # "division": "Platform Engineering",
            # "ckRoleID": "ENG-3",
            # "ckWorkerType": "Employee",
            # "ckLocation": "Oakland",
            # "countryCode": "US",
            # "ckOriginalHireDate": "2016-10-31",
            # "ckDepartmentCode": "Engineering_Department",
            # "state": "California",
            # "department": "Engineering",
            # "ckDivisionCode": "Platform Engineering_Division",
            # "ckJobProfile": 2007,
            # "email": "tim.johnson@ckcorptest.com",
            # "ckCostCenterCode": 120000,
            # "manager": "anson.lee",
            # "costCenter": "Information Technology",
            # "opsbotteam": "Corporate Reliability Engineering",
            # "secondEmail": "",
            # "shortname2": "tim.johnson",
            # "managerId": "0f217b2d59a61057691c991f98b34f5a",
            # "userName": "tim.johnson",
            # "ckDivision": "Platform Engineering",
            # "ckSubdivisionCode": "Information Technology_Sub_Division",
            # "ckWorkerSubType": "Regular",
            # "firstName": "Tim",
            # "ckSubdivision": "Information Technology (IT)",
            # "mobilePhone": "-",
            # "streetAddress": "1100 BROADWAY",
            # "ckHireDate": "2016-10-31",
            # "organization": "Credit Karma, Inc."



    return user_json

#########################################################################################################
# Name: Sync Okta Users to SecZetta
# Parameters:
#   users: An array of SecZetta users that are ready to be created/updated
# Purpose: 
#   Takes an array of users, checks the cache file to see if a certain users already exists (updates if 
#   so) and creates the users that dont exist. 
# Returns:
#   stats - a dictionary of the statistics of current run
#      user_count - count of the total users being passed into function
#      total_users_created - integer of the number of creates processed
#      total_users_updated - integer of the number of updates processed
#      success - boolean that indicates if the run completed without any errors
#########################################################################################################
def syncOktaUsersToSecZetta(users):
    global OKTA_CACHE_LOADED

    stats = {
        "user_count": len(users),
        "total_users_created": 0,
        "total_users_updated": 0,
        "success": True,
    }

    if OKTA_CACHE_LOADED == False:
        log.info("Okta Cache isn't loaded. Loading....")
        if not exists(OKTA_USER_CACHE_FILE_PATH):
            log.warning("No Cache File Exists at %s. Creating Blank one.", OKTA_USER_CACHE_FILE_PATH)
            f = open(OKTA_USER_CACHE_FILE_PATH, "w")
            f.write("okta_id,sz_id")
            f.close()
        else:
            with open(OKTA_USER_CACHE_FILE_PATH) as cache_file:
                csv_reader = csv.reader(cache_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        okta_id = row[0]
                        sz_id = row[1]
                        OKTA_CACHE[okta_id] = sz_id
                        line_count += 1
                log.info("Okta Cache Loaded! %s company ids were loaded.", line_count-1)
        OKTA_CACHE_LOADED = True

        for user in users:
            okta_id = user["profile"]["attributes"]["okta_id_ne_attribute"]
            if okta_id in OKTA_CACHE:
                log.info("User already in cache. Update?")
                sz_id = OKTA_CACHE[okta_id]
                response = sendAPIRequest("PATCH", "/profiles/" + sz_id, user)
                if response.status_code == 200:
                    stats["total_users_updated"] += 1
                    log.info("Successfully Updated User!")
                else:
                    log.error("Update User Failed! Status Code: %s. Quitting", response.status_code)
                    stats["success"] = False
                    return stats
            else:
                log.info("User not in cache. Create!")
                #response = sendAPIRequest("POST", "/profile", user)
                response = launchCreateWorkflow("8b5629d6-adc9-4626-a5bd-560cf873d754","8673441a-6c31-49fc-a687-e78927734ab7", "NeprofileUser", user["profile"]["attributes"])
                if response.status_code == 200 or response.status_code == 201:
                    log.info("Successfully Created User! %s", response.status_code)
                    stats["total_users_created"] += 1
                    #cacheOktaUser(okta_id, response.json()["profile"]["id"] )
                else:
                    stats["success"] = False
                    log.error("Create User Failed! Status Code: %s. Quitting", response.status_code)
                    log.error("%s", response.json())
                    return
        return stats

#########################################################################################################
# Name: Cache Okta User
# Parameters:
#   okta_id: The ID of the Okta user object
#   sz_id: The SecZetta ID when created
# Purpose: 
#   Stores the okta_id and seczetta_id mapping in order to quickly tell if a user exists or not.
#   As of right now, it just writes these data elements to a cache file. Could think about doing 
#   something specific with cache.
# Returns:
#   None
#########################################################################################################             
def cacheOktaUser(okta_id, sz_id):
    if not exists(OKTA_USER_CACHE_FILE_PATH):
        log.critical("FILE NOT FOUND: " + csv_full_path)
        exit()

    f = open(OKTA_USER_CACHE_FILE_PATH, "a")
    f.write("\n"+okta_id +","+sz_id)
    f.close()

#########################################################################################################
# Name: Launch Create Workflow
# Parameters:
#   workflow_id: The ID of the create workflow you want to launch
#   requester_id: The ID of the requester who should launch this workflow
#   requester_type: The type of requester (NeProfileUser / NeAccessUser)
#   attributes: a dictionary of attributes needed to pass to the workflow
# Purpose: 
#   Launches a workflow session in SecZetta
# Returns:
#   HTTP Response from the /workflow_sesssions API endpoint
#########################################################################################################
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



sz_users = getOktaUsersByGroup("00gn3nruy0J4QnrlU0h7")
stats = syncOktaUsersToSecZetta(sz_users)
log.info("Run Stats: %s", stats)