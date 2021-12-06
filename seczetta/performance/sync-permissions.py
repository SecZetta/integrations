from os import sync
import requests
from random import randrange
import time
from os.path import exists
import logging as log
import math
import csv
from datetime import datetime
import marriott


log.basicConfig(level=log.INFO)


from requests.api import get

# Base Config
#PERFORMANCE
#API_BASE = "https://marriottperformancedev.nonemployee.com/api"
#API_KEY = "18bae8c5f1944a71a502721ba460b18d"
#DEV
API_BASE = "https://marriottdev.nonemployee.com/api"
API_KEY = "5f7a5b07d07643609833787faee57d97"

PEOPLE_PROFILE_TYPE_ID = "1bd99a83-57e1-4e3c-bbb0-861b4700cff6"
USER_GARBAGE_CAN_USER = "bcde2b6c-69d0-44fa-85d4-29db11027631"
PROFILE_TYPE_ID_COMPANIES = "57ad1a76-9bbe-48d3-825e-4a967ab3f372"
PROFILE_TYPE_ID_PROPERTIES = "47e9fe1b-003f-4be6-90aa-f852aadb5628"
PROFILE_TYPE_ID_NON_ASSOCIATES = "f6eca1ce-db43-41cf-b32a-806419ec9595"
ATTRIBUTE_ID_COMPANY_NAME = "a7a9abc0-8e24-4c58-a0c9-6d7fb3bc6d69"
ATTRIBUTE_ID_PROPERTY_NAME = "6d5a37ba-d365-4ce6-aba6-4849a800c08d"
ATTRIBUTE_ID_PROPERTY_MANAGEMENT_COMPANY = "1a92bea4-78b7-4e9e-957b-79ab9665ada3"
ATTRIBUTE_ID_PROPERTY_OWNER_COMPANY = "72031d62-4203-4d60-86d2-5982aaa675e4"
ATTRIBUTE_ID_PROPERTY_FRANCHISEE_COMPANY = "0d2641c7-cf2d-4cd0-8ea5-d19b465b87f0"
ATTRIBUTE_ID_SYNC_STATUS = "ac94b1eb-9638-4029-b687-440e00b2dc21"
ATTRIBUTE_OPTION_ID_SYNC_STATUS_SYNCED = "39ef2d99-6ac1-43ca-bd38-941dfca44ab1"
ATTRIBUTE_OPTION_ID_SYNC_STATUS_NOT_SYNCED = "68ab1b04-b732-4cce-9bca-efb589de6509"
ATTRIBUTE_ID_LAST_SYNC_DATE = "76664617-1854-45e3-b035-649be3b6cb58"
ATTRIBUTE_ID_NON_ASSOCIATE_PROPERTY = "aa29a165-f767-4ff3-8f74-d296341e0bde"
INCREMENTAL_ID = 1
ROLE_ID_CACHE_FILE_PATH = marriott.CACHED_FOLDER + "cache-role-ids.cache"
ROLE_ID_CACHE_LOADED = False

RANDOM_FIRST = []
RANDOM_LAST = []
RANDOM_AREA_CODE = []

#Storage
ROLE_DICT = {}
TODAY = datetime.today().strftime('%m/%d/%Y')



### HELPER FUNCTIONS ###

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
# Archived Functions (for now)
# this was just me messing around with the API's that are avialable
#########################################################################################################

def setContributors(importFile = None, role_id = None):

    if importFile == None:

        global_admin_id = "29d10274-98a9-4e91-8846-36395acf958f"
        global_viewer_id = "59d2c500-cb1d-4f98-bc70-03e619aa07e0"
        property_admin_jw = "3371e6c0-9657-45e9-92e7-42fbc7a0a8fe"
        property_admin_rcc = "06a5c867-a04d-4425-8f95-b8a3a581b9d5"

        profile_ids = [
            "055d0bfa-5aab-4c6c-bd1c-6c20176006d8",
            "18677e11-bd1d-493c-8541-45c46b7850a9",
            "2172d107-c98d-4d6e-bb01-728ebf72a726",
            "3b8b5bd5-47ea-485e-ae9d-052f6b63409c",
            "3f8f4071-a85a-42c1-a378-e4d77539f098",
            "4bede99b-5bb0-4870-8fdd-114bc5558972",
            "4d2297c0-8b80-4204-8aa5-764ddb1cf854",
            "5ff5c873-45ec-454b-8e5e-747d5e9f056c",
            "6eebdf16-9e46-4276-a6b5-4d000d48c651",
            "7c74dc8c-01e1-400a-9bcc-a32db7bf4142",
            "8623c099-2b86-4291-a9a7-43af51198691",
            "946cf184-c28d-478c-8930-792b6557ebdc",
            "9d1028ff-184a-46a5-acb7-de14d5c0665b",
            "aee3f60b-b95d-4ed5-bd6a-1c963296db9c",
            "c01e02da-9a4a-4e3f-9fe7-0c87d739fd73",
            "c46a90f6-25ed-4714-9337-272b441f87ff",
            "c829de3a-ceec-49c1-aead-8a7302b51309",
            "cbb389c3-89d7-4fb6-a3b1-c040bb971733",
            "d2899a43-af38-43f2-86d6-4e012b74d5ae",
            "e39844ae-ae33-4667-813e-f8257fd686e2",
            "e98bb51b-36ab-4756-86f1-9316a67a695a",
            "fd40104d-2311-45f8-8aa3-3df07738b1b1",
            "0d7edee3-44bf-4272-a500-771c8813d61f",
            "1c3afb20-fbaf-4176-a615-79373d5f552f",
            "3dbc2e1d-2433-4c64-baec-7673ff254a8c",
            "a9f58799-ef0a-4660-806c-4dbe356714ed",
            "f48c72bc-e1f1-4f73-a56d-93a44c693d8f",
            "0b951d5c-3f10-4b3b-a587-024770bdec55",
            "20e06feb-0519-451c-8a8c-f8c7664fec38",
            "31feda3e-19d3-4a4c-8a4f-5711f7fb09ad",
            "3f179f01-ac29-4f9d-ab5f-eb50661aeddb",
            "8daa7ea4-225a-4b34-8d60-2cb4b5306aef",
            "93f88bfd-138b-4531-8113-387d37f18f4f",
            "983a1e8b-e5e5-48b8-b199-ae27a5acfed6",
            "cf58c693-66a6-4334-b3f7-bd7258855567",
            "f0372411-e040-4543-bea2-0bd4bd30c95b",
            "0b4539f1-17c9-4607-a3de-4d630b62ca08",
            "7d2eac5c-325e-4039-94e4-0eea72d80a88",
            "e69d1eab-1110-4824-81ad-7b10925715be",
            "eb63e4cf-2e71-495b-8fe3-efad7e9adfac",
            "f58306df-6d50-4631-9513-783a2c588364"
        ]

        for profile_id in profile_ids:

            data = {
                "role_profiles": [
                    {
                        "role_id": global_admin_id,
                        "profile_id": profile_id
                    },
                    {
                        "role_id": global_viewer_id,
                        "profile_id": profile_id
                    }
                ]
            }

            print(sendAPIRequest("POST", "https://jendemo.mynonemployee.com/api/role_profiles", data))
    else:
        #use import file
        if exists(importFile) and role_id != None:
            #file exists continue
            role_profiles = []
            with open(importFile, 'r') as f:
                f.readline()  # skip first line
                for id in f:
                    id = id.strip()
                    if id.startswith("\""):
                        id = id[1:len(id)-1]
                    rp = {
                        "role_id": role_id,
                        "profile_id": id
                    }
                    role_profiles.append(rp)
            
            data = {}
            data["role_profiles"] = role_profiles
            print(sendAPIRequest("POST","/role_profiles", data))

        else:
            print("ERROR: File: " + importFile +" doesnt exist. Or No RoleID specified")

def initializeRandomData():
    with open('random-first.csv', 'r') as f:
        f.readline()  # skip first line
        for name in f:
            RANDOM_FIRST.append(name.strip())
    with open('random-last.csv', 'r') as f:
        f.readline()  # skip first line
        for name in f:
            RANDOM_LAST.append(name.strip())
    with open('random-area-code.csv', 'r') as f:
        f.readline()  # skip first line
        for code in f:
            RANDOM_AREA_CODE.append(code.strip())

def getRandom(attribute):
    
    if(attribute == "first_name"):
        return RANDOM_FIRST[randrange(len(RANDOM_FIRST))]
    elif(attribute == "last_name"):
        return RANDOM_LAST[randrange(len(RANDOM_LAST))]
    elif(attribute == "phone"):
        area_code = RANDOM_AREA_CODE[randrange(len(RANDOM_AREA_CODE))]
        phone = "(" + area_code + ")"

        for i in range(1, 4):
            phone += str(randrange(1,10))
        
        phone += "-"

        for i in range(1, 5):
            phone += str(randrange(10))
        
        return phone
        
    else:
        return None

def createPerson():
    global INCREMENTAL_ID

    data = {
        "profile": {
            "profile_type_id": PEOPLE_PROFILE_TYPE_ID,
            "status": 1,
            "attributes": {
                "profile_id": "SZ" + str(INCREMENTAL_ID).zfill(9),
                "personal_first_name": getRandom("first_name"),
                "personal_last_name": getRandom("last_name"),
                "role": "Property Non-Associate"
                
            }
        }
    }
    
    response = sendAPIRequest("POST", "/profile", data)

    if response.status_code == 201:
        INCREMENTAL_ID += 1

    return response.status_code
    #return response.json()


#########################################################################################################
# Name: Sync Companies
# Purpose: 
#   As of now this grabs ALL companies and loops thru them adding the required roles as contributors
#   This includes global admin, seczetta, admin, etc. Also, this checks to see if the company role is created
#    and if not it creates it and assigns it to the company profile
#########################################################################################################
def syncCompanies():
    global ROLE_DICT
    #grab all the companies using the advance search
    
    
    total_synced = 0
    limit = 75
    offset = 0
    sync_still_required = True

    advanced_search_data = {
        "advanced_search": {
            "condition_rules_attributes": [
                {
                    "type": "ProfileTypeRule",
                    "comparison_operator": "==",
                    "value": PROFILE_TYPE_ID_COMPANIES
                },
                {
                        "type": "ProfileAttributeRule",
                        "condition_object_id": ATTRIBUTE_ID_SYNC_STATUS,
                        "object_type": "NeAttribute",
                        "comparison_operator": "!=",
                        "value": ATTRIBUTE_OPTION_ID_SYNC_STATUS_SYNCED
                }

            ]
        }
    }
    while sync_still_required:
        synced_companies = []
        url = "/advanced_search/run?query[limit]="+str(limit)+"&query[offset]="+str(offset)
        log.info("Grabbing Companies: Limit: %s, Offset %s. Total Synced So Far: %s", limit, offset, total_synced)
        companies_response = sendAPIRequest("POST", url, advanced_search_data)
        companies_response_json = {}
        if companies_response.status_code == 200:
            companies_response_json = companies_response.json()
        else:
            log.error("Error Occurred. Status Code: %s", companies_response.status_code)
            log.error("Error Message: %s", companies_response.json())
            exit()
        
        company_profiles = companies_response_json["profiles"]
        if len(company_profiles) == 0:
            log.info("Success! All Companies have been synced. %s companies were synced on this run", total_synced)
            sync_still_required = False
            return
        #role_profiles stores the different contributor relationships we will be setting
        role_profiles = []

        #loop through the companies to being the sync process
        for c in companies_response_json["profiles"]:
            attributes = c["attributes"]
            #pythons conditional operator
            id = c["id"]
            account_id = attributes["company_account_id"] if "company_account_id" in attributes else None
            name = attributes["company_name"] if "company_name" in attributes else None
            log.info("Found Company that requires Sycing: %s", name)

            if account_id == None:
                log.warning("Company had no AccountID. Skipping")
                continue

            #always add these 3 roles to all company profiles
            #TODO: make this an array so its cleaner
            rp = {
                "role_id": ROLE_DICT["SecZetta Administrator"],
                "profile_id": id
            }
            role_profiles.append(rp)
            rp = {
                "role_id": ROLE_DICT["Global Administrator"],
                "profile_id": id
            }
            role_profiles.append(rp)
            rp = {
                "role_id": ROLE_DICT["Global Administrator - View Only"],
                "profile_id": id
            }
            role_profiles.append(rp)

            #Lets make sure there is a role for each company.
            role_name = "Company - " + account_id
            if role_name not in ROLE_DICT:
                new_id = createRole(role_name)
                ROLE_DICT[role_name] = new_id

            #add the company role to the company
            rp = {
                "role_id": ROLE_DICT[role_name],
                "profile_id": id
            }
            role_profiles.append(rp)
            synced_companies.append(id)


        #now we've looped through the companies and added all the contributor relationships to role_profiles.
        #I dont want to send one request with an array of 1000+ elements. Use batch quantity to set the number
        # of elements per request. Set to 50 by default
        batch_quantity = 50
        tmp = []
        log.info(len(role_profiles))
        for i in range(0,len(role_profiles)):
            log.info("LOOPING!")
            log.info(role_profiles[i])
            tmp.append(role_profiles[i])
            if i % batch_quantity == 0:
                data = {}
                data["role_profiles"] = tmp
                log.info(sendAPIRequest("POST","/role_profiles", data).json())
                tmp = []
        data = {}
        data["role_profiles"] = tmp
        log.info(sendAPIRequest("POST","/role_profiles", data).json())

        #now that we've sync'ed the company we need to set their sync status. We will do this in batches too
        batch_quantity = 50
        tmp = []
        log.info(len(synced_companies))
        for i in range(0,len(synced_companies)):
            log.info("LOOPING COMPANIES")
            tmp_data = {
                "id": synced_companies[i],
                "attributes": {
                    "sync_status": "Synced",
                    "last_synced_date": TODAY
                }
            }
            tmp.append(tmp_data)
            if i % batch_quantity == 0:
                data = {}
                data["profiles"] = tmp
                log.info(sendAPIRequest("PATCH","/profiles", data).json())
                tmp = []
        if len(tmp) > 0:
            data = {}
            data["profiles"] = tmp
            log.info(sendAPIRequest("PATCH","/profiles", data).json())

        total_synced += len(synced_companies)
        offset += limit

            
#########################################################################################################
# Name: Sync Properties
# Purpose: 
#   As of now this grabs ALL properties and loops thru them adding the required roles as contributors
#   This includes global admin, seczetta, admin, etc. Also, this checks to see if the property role is created
#    and if not it creates it and assigns it to the property profile
#########################################################################################################  
def syncProperties():
    total_synced = 0
    limit = 75
    offset = 0
    sync_still_required = True

    advanced_search_data = {
        "advanced_search": {
            "condition_rules_attributes": [
                {
                    "type": "ProfileTypeRule",
                    "comparison_operator": "==",
                    "value": PROFILE_TYPE_ID_PROPERTIES
                },
                {
                        "type": "ProfileAttributeRule",
                        "condition_object_id": ATTRIBUTE_ID_SYNC_STATUS,
                        "object_type": "NeAttribute",
                        "comparison_operator": "!=",
                        "value": ATTRIBUTE_OPTION_ID_SYNC_STATUS_SYNCED
                }

            ]
        }
    }
    while sync_still_required:
        synced_properties = []
        url = "/advanced_search/run?query[limit]="+str(limit)+"&query[offset]="+str(offset)
        log.info("Grabbing Properties: Limit: %s, Offset %s. Total Synced So Far: %s", limit, offset, total_synced)
        properties_response = sendAPIRequest("POST", url, advanced_search_data)
        properties_response_json = {}
        if properties_response.status_code == 200:
            properties_response_json = properties_response.json()
        else:
            log.error("Error Occurred. Status Code: %s", properties_response.status_code)
            log.error("Error Message: %s", properties_response.json())
            exit()
        

        property_profiles = properties_response_json["profiles"]
        if len(property_profiles) == 0:
            log.info("Success! All Properties have been synced. %s properties were synced on this run", total_synced)
            sync_still_required = False
            return

        role_profiles = []

        log.info(len(properties_response_json["profiles"]))

        for p in properties_response_json["profiles"]:
            attributes = p["attributes"]
            #pythons conditional operator
            id = p["id"]
            name = attributes["property_name"] if "property_name" in attributes else None
            property_id = attributes["property_id"] if "property_id" in attributes else None
            
            log.info("Processing Property %s (%s)",name,id)

            rp = {
                "role_id": ROLE_DICT["SecZetta Administrator"],
                "profile_id": id
            }
            role_profiles.append(rp)
            rp = {
                "role_id": ROLE_DICT["Global Administrator"],
                "profile_id": id
            }
            role_profiles.append(rp)
            rp = {
                "role_id": ROLE_DICT["Global Administrator - View Only"],
                "profile_id": id
            }
            role_profiles.append(rp)

            #Lets make sure there is a role for each property.
            role_name = "Property - " + property_id
            if role_name not in ROLE_DICT:
                new_id = createRole(role_name)
                ROLE_DICT[role_name] = new_id

            #add the company role to the property
            rp = {
                "role_id": ROLE_DICT[role_name],
                "profile_id": id
            }
            role_profiles.append(rp)
            synced_properties.append(id)
            #now add to the non-associates
            non_associates_json = getNonAssociatesByProperty(id)
            if non_associates_json is not None:
                for na in non_associates_json:
                    user_id = na["id"]
                    role_profiles.append({
                        "role_id": ROLE_DICT[role_name],
                        "profile_id": user_id
                    })
                    role_profiles.append({
                        "role_id": ROLE_DICT["SecZetta Administrator"],
                        "profile_id": user_id
                    })
                    role_profiles.append({
                        "role_id": ROLE_DICT["Global Administrator"],
                        "profile_id": user_id
                    })
            else:
                log.warning("Property: %s (%s) has no non-associates assigned to it.", name, id)

        tmp = []
        for i in range(0,len(role_profiles)):
            tmp.append(role_profiles[i])
            if i % 50 == 0:
                data = {}
                data["role_profiles"] = tmp
                log.info(sendAPIRequest("POST","/role_profiles", data).json())
                tmp = []
        data = {}
        data["role_profiles"] = tmp
        log.info(sendAPIRequest("POST","/role_profiles", data).json())

        #now that we've sync'ed the company we need to set their sync status. We will do this in batches too
        batch_quantity = 50
        tmp = []
        for i in range(0,len(synced_properties)):
            tmp_data = {
                "id": synced_properties[i],
                "attributes": {
                    "sync_status": "Synced",
                    "last_synced_date": TODAY
                }
            }
            tmp.append(tmp_data)
            if i % batch_quantity == 0:
                data = {}
                data["profiles"] = tmp
                log.info(sendAPIRequest("PATCH","/profiles", data).json())
                tmp = []
        if len(tmp) > 0:
            data = {}
            data["profiles"] = tmp
            log.info(sendAPIRequest("PATCH","/profiles", data).json())

        total_synced += len(synced_properties)
        offset += limit


#########################################################################################################
# Name: Get Roles
# Purpose: 
#   This grabs all of the roles in the system and puts them into a global variable called `ROLE_DICT`
#   This variable is a dictionary with the name as the key and the role_id as the value. this way you can
#   easily grab the role you want just by calling ROLE_DICT["Global Administrator"] and you will get the
#   SecZetta role_id
#########################################################################################################               
def getRoles(fullCacheReset = False):
    global ROLE_DICT, ROLE_ID_CACHE_LOADED

    limit = 200
    total_offsets = 0
    #grab the current roles
    if fullCacheReset:
        with open(ROLE_ID_CACHE_FILE_PATH, "w") as file:
            file.write("role_name,role_id")
        cache_response = sendAPIRequest("GET","/roles?query[limit]=1&query[offset]=0&metadata=true", {})
        if cache_response.status_code == 200:
            cache_json = cache_response.json()
            metadata = cache_json["_metadata"]
            total_roles = metadata["total"]
            total_offsets = math.ceil(total_roles/limit)
            log.info("Got Total Roles: %s, which means there will be %s total calls with limit of %s", total_roles, total_offsets, limit)
        else:
            log.critical("Something went wrong Getting Role Meta data. Status Code: %s",cache_response.status_code)
            exit()

        if total_offsets == 0:
            log.error("Couldnt get total offsets..")
            return None

        for offset in range(0,total_offsets):
            new_offset = offset * limit
            tmp_url = "/roles?query[limit]="+str(limit)+"&query[offset]=" + str(new_offset)
            log.info("Getting Role Cache. API Call #%s. Url: %s", offset+1, tmp_url)
            tmp_response = sendAPIRequest("GET",tmp_url, {})
            if tmp_response.status_code == 200:
                for role in tmp_response.json()["roles"]:
                    ROLE_DICT[role["name"]] = role["id"]
                    cacheRoleIds(role["name"], role["id"])
        ROLE_ID_CACHE_LOADED = True

    if ROLE_ID_CACHE_LOADED == False:
        with open(ROLE_ID_CACHE_FILE_PATH) as cache_file:
            csv_reader = csv.reader(cache_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    role_name = row[0]
                    role_id = row[1]
                    ROLE_DICT[role_name] = role_id
                    line_count += 1
            log.info("Role ID Cache Loaded! %s role ids were loaded.", line_count-1)
        ROLE_ID_CACHE_LOADED = True

    #Create the ones that dont exist that are required
    required_roles = [
        "SecZetta Administrator",
        "Global Administrator",
        "Global Administrator - View Only",
        "Company Access Admin",
        "Property Access Admin"
    ]
    for r in required_roles:
        if r not in ROLE_DICT:
            new_id = createRole(r)
            ROLE_DICT[r] = new_id

def cacheRoleIds(role_name, role_id):
    if not exists(ROLE_ID_CACHE_FILE_PATH):
        log.warning("No Cache File Exists at %s. Creating Blank one.", ROLE_ID_CACHE_FILE_PATH)
        f = open(ROLE_ID_CACHE_FILE_PATH, "w")
        f.write("role_name,role_id")
        f.close()

    f = open(ROLE_ID_CACHE_FILE_PATH, "a")
    f.write("\n"+role_name +","+role_id)
    f.close()


#########################################################################################################
# Name: Create Role
# Paramters:
#   name: the name of the role you want to create
# Purpose: 
#   This is a helper function that creates a role based on the passed in string 'name'.
# Return Value:
#   the ID of the newly created role (if successfully created). If something failed, it will return
#   'None'
#########################################################################################################    
def createRole(name):
    log.info("Entering createRole() - %s",name)
    uid = name.replace(" ","_").lower()
    uid = uid.replace("&","and")
    uid = uid.replace("/","_")
    uid = uid.replace(".","")
    uid = uid.encode("ascii", "ignore").decode()

    data = {
        "role": {
            "name": name,
            "uid": uid,
            "groups": [
                uid
            ]
        }
    }

    create_response = sendAPIRequest("POST", "/role", data)
    if create_response.status_code == 200 or create_response.status_code == 201:
        json = create_response.json()
        log.info("["+name+"] Role was successfully created! ID: " + json["role"]["id"])
        return json["role"]["id"]
    else:
        log.error("ERROR OCCURRED DURING CREATE ROLE")
        log.error(create_response.json())
        return None

#########################################################################################################
# Name: Delete Roles From User
# Paramters:
#   user_id: the SecZetta ID of the user in question
# Purpose: 
#   This is a helper function that 'deletes' the roles from a specific user. The word deletes is in quotes
#   because currently there is no API that allows for deletion. We just patch the user_role onto another 
#   'dummy user' to remove them off the current user
# Return Value:
#   Status Code (200) for Success, 400 for failure
#########################################################################################################
def deleteRolesFromUser(user_id):

    role_ids_to_remove = []
    user_roles_response = sendAPIRequest("GET", "/user_roles?user_id="+user_id, {})
    if user_roles_response.status_code == 200:
        if "error" in user_roles_response.json():
            log.info("User doesnt have any roles. No need to delete!")
            return

        user_roles = user_roles_response.json()["user_roles"]
        for role in user_roles:
            log.info("Role:" + role["id"])
            role_ids_to_remove.append(role["id"])
    

    role_relationships = []
    for role_id in role_ids_to_remove:
        role_relationships.append({
            "id": role_id,
            "user_id": USER_GARBAGE_CAN_USER
        })


    data = {
        "user_roles": role_relationships
    }
    return sendAPIRequest("PATCH", "/user_roles", data).status_code

#########################################################################################################
# Name: Get Properties
# Paramters:
#   attribute_id: this is the SecZetta ID for the attribute we want to filter on
#   company_id: this is the company_id we want to compare to the property attribute
# Purpose: 
#   This name isnt the best, but the purpose of this function is to be able to get all of the different
#   properties that are related in some way (managed, owned, franchised) to a company
# Return Value:
#   Json response of properties
#########################################################################################################
def getProperties(attribute_id, company_id):
    log.info("Entering getProperties %s %s", attribute_id, company_id)
    data = {
        "advanced_search": {
            "label": "Get Properties",
            "condition_rules_attributes": [
                {
                    "type": "ProfileTypeRule",
                    "comparison_operator": "==",
                    "value": PROFILE_TYPE_ID_PROPERTIES
                },
                {
                    "type": "ProfileAttributeRule",
                    "condition_object_id": attribute_id,
                    "object_type": "NeAttribute",
                    "comparison_operator": "include?",
                    "value": company_id
                }
            ]
        }
    }
    properties_response = sendAPIRequest("POST", "/advanced_search/run", data)
    if properties_response.status_code == 200:
        log.info("Success. Returning Properties JSON response")
        return properties_response.json()
    else:
        log.error("Error. Something went wrong with the get properties advanced search")
        log.error(properties_response.json())
        return None

def getNonAssociatesByProperty(property_id):
    log.info("Entering getNonAssociatesByProperty %s", property_id)
    data = {
        "advanced_search": {
            "label": "Get Properties",
            "condition_rules_attributes": [
                {
                    "type": "ProfileTypeRule",
                    "comparison_operator": "==",
                    "value": PROFILE_TYPE_ID_NON_ASSOCIATES

                },
                {
                    "type": "ProfileAttributeRule",
                    "condition_object_id": ATTRIBUTE_ID_NON_ASSOCIATE_PROPERTY,
                    "object_type": "NeAttribute",
                    "comparison_operator": "include?",
                    "value": property_id
                }
            ]
        }
    }

    non_associate_response = sendAPIRequest("POST", "/advanced_search/run", data)
    if non_associate_response.status_code == 200:
        log.info("Success. Returning Properties JSON response")
        return non_associate_response.json()["profiles"]
    else:
        log.error("Error. Something went wrong with the get properties advanced search")
        log.error(non_associate_response.json())
        return None

#########################################################################################################
# Name: Get User
# Paramters:
#   param: defaults to login, but could also do things like email
#   value: the value of the param so if email it the value would be something like thook@seczetta.com
# Purpose: 
#   This function will return a user in json format based on the parameters supplied
# Return Value:
#   On Success: JSON representation of a user
#   On Error: None
#########################################################################################################
def getUser(param="login", value="Norman.Davidson"):
    log.info("Entering getUser [%s %s]", param, value)
    user_response = sendAPIRequest("GET", "/users?"+param+"="+value, {})
    if user_response.status_code == 200:
        log.info("Success. Got User. Returning..")
        return user_response.json()["users"][0]
    else:
        log.error("Error. Something went wrong with getting users")
        return None
   
#########################################################################################################
# Name: Impersonate
#
# WARNING: THIS REMOVES ALL EXSITING ROLES AND REPLACES THEM FOR THIS PORTAL USER
#
# Paramters:
#   user_login: The login for the portal user we want to update
#   role_type: Company Access Admin, Property Access Admin, or Global Administrator
#   profile_name: when role_type is Company Access Admin or Property Access Admin, the company/property name
#                 is required
# Purpose: 
#   This function was built to easily be able to change permissions on users for the various different
#   actors in the Marriott environment 
#########################################################################################################
def impersonate(user_login, role_type, profile_name):
    global ROLE_DICT

    ## first get the portal user from login
    user_json = getUser("login", user_login)

    if user_json == None:
        log.critical("User Not Found. Failing!")
        return

    deleteRolesFromUser(user_json["id"])

    if role_type == "Company Access Admin":
        data = {
            "advanced_search": {
                "label": "Get All Companies",
                "condition_rules_attributes": [
                    {
                        "type": "ProfileTypeRule",
                        "comparison_operator": "==",
                        "value": PROFILE_TYPE_ID_COMPANIES
                    },
                    {
                        "type": "ProfileAttributeRule",
                        "condition_object_id": ATTRIBUTE_ID_COMPANY_NAME,
                        "object_type": "NeAttribute",
                        "comparison_operator": "include?",
                        "value": profile_name
                    }
                ]
            }
        }
        company_response = sendAPIRequest("POST", "/advanced_search/run", data)

        if company_response.status_code == 200:
            company_json = company_response.json()["profiles"][0]
            company_id = company_json["attributes"]["company_account_id"]
            managed_properties_response = getProperties(ATTRIBUTE_ID_PROPERTY_MANAGEMENT_COMPANY, company_json["id"])
            owned_properties_response = getProperties(ATTRIBUTE_ID_PROPERTY_OWNER_COMPANY, company_json["id"])
            franchised_properties_response = getProperties(ATTRIBUTE_ID_PROPERTY_FRANCHISEE_COMPANY, company_json["id"])

            properties = {}
            if managed_properties_response is not None:
                for p in managed_properties_response["profiles"]:
                    property_name = p["name"]
                    property_id = p["attributes"]["property_id"]
                    if property_id in properties:
                        continue
                    else:
                        properties[property_id] = p

            if owned_properties_response is not None:
                for p in owned_properties_response["profiles"]:
                    property_name = p["name"]
                    property_id = p["attributes"]["property_id"]
                    if property_id in properties:
                        continue
                    else:
                        properties[property_id] = p


            if franchised_properties_response is not None:
                for p in franchised_properties_response["profiles"]:
                    property_name = p["name"]
                    property_id = p["attributes"]["property_id"]
                    if property_id in properties:
                        continue
                    else:
                        properties[property_id] = p

            #name is the key of the dictionary
            add_user_roles = []
            for id in properties:
                user_role_relationship = {
                    "role_id": ROLE_DICT["Property - " + id],
                    "user_id": user_json["id"]
                }
                add_user_roles.append(user_role_relationship)

            #add company role
            add_user_roles.append({
                "role_id": ROLE_DICT["Company - " + company_id],
                "user_id": user_json["id"]
            })
            #add Company Access Admin
            add_user_roles.append({
                "role_id": ROLE_DICT["Company Access Admin"],
                "user_id": user_json["id"]
            })

            #add portal access
            add_user_roles.append({
                "role_id": ROLE_DICT["NAP Portal Access"],
                "user_id": user_json["id"]
            })
            data = {
                "user_roles": add_user_roles
            }
            sendAPIRequest("POST","/user_roles", data)

    if role_type == "Property Access Admin":

        add_user_roles = []

        #add Property role
        add_user_roles.append({
            "role_id": ROLE_DICT["Property - " + profile_name],
            "user_id": user_json["id"]
        })
        #add Property Access Admin
        add_user_roles.append({
            "role_id": ROLE_DICT["Property Access Admin"],
            "user_id": user_json["id"]
        })
        #add portal access
        add_user_roles.append({
            "role_id": ROLE_DICT["NAP Portal Access"],
            "user_id": user_json["id"]
        })
        data = {
            "user_roles": add_user_roles
        }
        sendAPIRequest("POST","/user_roles", data)

    if role_type == "Global Administrator":
        add_user_roles = []
        add_user_roles.append({
            "role_id": ROLE_DICT["Global Administrator"],
            "user_id": user_json["id"]
        })
        #add portal access
        add_user_roles.append({
            "role_id": ROLE_DICT["NAP Portal Access"],
            "user_id": user_json["id"]
        })
        data = {
            "user_roles": add_user_roles
        }
        sendAPIRequest("POST","/user_roles", data)

#setContributors("contribs.csv","22dacaf3-9a4f-4b14-a733-1e9d1cd91991")
#initializeRandomData()




getRoles()
#syncCompanies()
#syncProperties()

#impersonate("Christopher.Ray", "Company Access Admin", "Meyer Jabara Hotels")
impersonate("Christopher.Ray", "Property Access Admin", "a1W1I000000aWypUAE")
#impersonate("Norman.Davidson", "Property Access Admin", "Towneplace Hotel - Kovda")
#impersonate("Norman.Davidson", "Global Administrator", "Orange Penguin Hotels")
#impersonate("Mark.Howera", "Global Administrator", "")


