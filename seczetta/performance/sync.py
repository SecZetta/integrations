from os import stat
import requests
from random import randrange
import time
from os.path import exists
import json
import logging as log
import pandas as pd
import time
from multiprocessing import Process, Queue
import random
import csv

log.basicConfig(level=log.INFO)


from requests.api import get

# Base Config
#PERFORMANCE
#API_BASE = "https://marriottperformancedev.nonemployee.com/api"
#API_KEY = "18bae8c5f1944a71a502721ba460b18d"
#DEV
API_BASE = "https://marriottdev.nonemployee.com/api"
API_KEY = "5f7a5b07d07643609833787faee57d97"

#Profile Types
PEOPLE_PROFILE_TYPE_ID = "1bd99a83-57e1-4e3c-bbb0-861b4700cff6"
PROFILE_TYPE_ID_COMPANIES = "57ad1a76-9bbe-48d3-825e-4a967ab3f372"
PROFILE_TYPE_ID_PROPERTIES = "47e9fe1b-003f-4be6-90aa-f852aadb5628"
PROFILE_TYPE_ID_NON_ASSOCIATES = "f6eca1ce-db43-41cf-b32a-806419ec9595"

#Company Globals
ATTRIBUTE_ID_COMPANY_ACCOUNT_ID = "acb31fd8-fc7d-4d44-aa72-1c987ae4ad4f"
ATTRIBUTE_ID_COMPANY_NAME = "a7a9abc0-8e24-4c58-a0c9-6d7fb3bc6d69"
SCHEMA_ATTRIBUTE_COMPANY_ID = "ACCT_ID"
SCHEMA_ATTRIBUTE_COMPANY_NAME = "acct_nm"
SCHEMA_ATTRIBUTE_STATUS = "acct_status_txt"
SCHEMA_ATTRIBUTE_PRIMARY_COMPANY_CODE = "PRIM_CD"
SCHEMA_ATTRIBUTE_SECONDARY_COMPANY_CODE = "SECONDARY_CD"
SCHEMA_ATTRIBUTE_ACCOUNT_TYPE = "ACCT_TYPE_FLOW_TXT"
SCHEMA_ATTRIBUTE_NALO_INTL = "NALO_INTL_TXT"
SCHEMA_ATTRIBUTE_REGION = "acct_region_txt"

#Property Globals
ATTRIBUTE_ID_PROPERTY_NAME = "6d5a37ba-d365-4ce6-aba6-4849a800c08d"
ATTRIBUTE_ID_PROPERTY_MANAGEMENT_COMPANY = "1a92bea4-78b7-4e9e-957b-79ab9665ada3"
ATTRIBUTE_ID_PROPERTY_OWNER_COMPANY = "72031d62-4203-4d60-86d2-5982aaa675e4"
ATTRIBUTE_ID_PROPERTY_FRANCHISEE_COMPANY = "0d2641c7-cf2d-4cd0-8ea5-d19b465b87f0"
SCHEMA_ATTRIBUTE_PROPERTY_ID = "prop_id"
SCHEMA_ATTRIBUTE_PROPERTY_NAME = "prop_nm"
SCHEMA_ATTRIBUTE_PROPERTY_MARSHA_CODE = "MARSHA_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_STATUS = "PROP_STATUS_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_REGION = "OPS_REGION_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_NALO_INTL = "NALO_INTL_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_BRAND = "brand_txt"
SCHEMA_ATTRIBUTE_PROPERTY_TYPE = "hotel_type_txt"
SCHEMA_ATTRIBUTE_PROPERTY_OWNER_TYPE = "OWNER_TYPE_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_LVL1_DIVISION = "DUD_DIVISION_CD"
SCHEMA_ATTRIBUTE_PROPERTY_LVL1_UNIT = "DUD_UNIT_CD"
SCHEMA_ATTRIBUTE_PROPERTY_LVL1_DEPARTMENT = "DUD_DEPT_CD"
SCHEMA_ATTRIBUTE_PROPERTY_LVL3_DIVISION = "PEOPLESOFT_ID_DIVISION"
SCHEMA_ATTRIBUTE_PROPERTY_LVL3_UNIT = "PEOPLESOFT_ID_UNIT"
SCHEMA_ATTRIBUTE_PROPERTY_LVL3_DEPARTMENT = "PEOPLESOFT_ID_DEPT"
SCHEMA_ATTRIBUTE_PROPERTY_MANAGEMENT_COMPANY = "PROP_MGR_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_OWNER_COMPANY = "PROP_OWNER_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_FRANCHISEE_COMPANY = "PROP_FRAN_TXT"
SCHEMA_ATTRIBUTE_PROPERTY_ASSET_MANAGEMENT_COMPANY = "PROP_AM_TXT"


ATTRIBUTE_ID_NON_ASSOCIATE_PROPERTY = "aa29a165-f767-4ff3-8f74-d296341e0bde"
INCREMENTAL_ID = 1

SCHEMA_CONVERSION_DICT = {
    SCHEMA_ATTRIBUTE_COMPANY_ID: "company_account_id",
    SCHEMA_ATTRIBUTE_COMPANY_NAME: "company_name",
    SCHEMA_ATTRIBUTE_STATUS: "company_status",
    SCHEMA_ATTRIBUTE_PRIMARY_COMPANY_CODE: "company_primary_company_code",
    SCHEMA_ATTRIBUTE_SECONDARY_COMPANY_CODE: "company_secondary_company_code",
    SCHEMA_ATTRIBUTE_ACCOUNT_TYPE: "company_account_type",
    SCHEMA_ATTRIBUTE_NALO_INTL: "company_nalo_intl",
    SCHEMA_ATTRIBUTE_REGION: "company_region",
    SCHEMA_ATTRIBUTE_PROPERTY_ID: "property_id",
    SCHEMA_ATTRIBUTE_PROPERTY_NAME: "property_name",
    SCHEMA_ATTRIBUTE_PROPERTY_MARSHA_CODE: "property_marsha_code",
    SCHEMA_ATTRIBUTE_PROPERTY_STATUS:"property_status",
    SCHEMA_ATTRIBUTE_PROPERTY_REGION: "property_region",
    SCHEMA_ATTRIBUTE_PROPERTY_NALO_INTL: "property_nalo_intl",
    SCHEMA_ATTRIBUTE_PROPERTY_BRAND: "property_brand",
    SCHEMA_ATTRIBUTE_PROPERTY_TYPE: "property_type",
    SCHEMA_ATTRIBUTE_PROPERTY_OWNER_TYPE: "property_owner_type",
    SCHEMA_ATTRIBUTE_PROPERTY_LVL1_DIVISION: "property_dud_lvl1_division",
    SCHEMA_ATTRIBUTE_PROPERTY_LVL1_UNIT: "property_dud_lvl1_unit",
    SCHEMA_ATTRIBUTE_PROPERTY_LVL1_DEPARTMENT: "property_dud_lvl1_department",
    SCHEMA_ATTRIBUTE_PROPERTY_LVL3_DIVISION: "property_dud_lvl3_division",
    SCHEMA_ATTRIBUTE_PROPERTY_LVL3_UNIT: "property_dud_lvl3_unit",
    SCHEMA_ATTRIBUTE_PROPERTY_LVL3_DEPARTMENT: "property_dud_lvl3_department",
    SCHEMA_ATTRIBUTE_PROPERTY_MANAGEMENT_COMPANY: "property_management_company",
    SCHEMA_ATTRIBUTE_PROPERTY_OWNER_COMPANY: "property_owner_company",
    SCHEMA_ATTRIBUTE_PROPERTY_FRANCHISEE_COMPANY: "property_franchisee_company",
    SCHEMA_ATTRIBUTE_PROPERTY_ASSET_MANAGEMENT_COMPANY: "property_access_management_company"
}

#Caching
CACHED_FOLDER = "data/cached/"
DATA_FOLDER= "data/"
COMPANY_CACHE_LOADED = False
COMPANY_CACHE_FILE_PATH = CACHED_FOLDER + "cache-company-ids.cache"
COMPANY_CACHE = {}

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

#########################################################################################################
# Name: Process Company File
# Parameters:
#   filename: The file name of the file we are going to process, this defaults to the data folder
#             and the cached folder.   
# Purpose: 
#   Processes the new company file. Typically this will be ran every 4 hours
#########################################################################################################
def processCompanyFile(filename):

    stats = {
        "total_creates": 0,
        "total_updates": 0,
        "total_deletes": 0,
        "sucessful_creates": 0,
        "sucessful_updates": 0,
        "sucessful_deletes": 0,
        "job_ids": []
    }

    #grab the file paths for both the regular file and the cached file
    cached_csv_full_path = CACHED_FOLDER + "cached-" + filename
    csv_full_path = DATA_FOLDER + filename
    #dataframes just help process CSV data quickly
    dfCached = pd.DataFrame()
    dfNew = pd.DataFrame()

    if not exists(csv_full_path):
        log.critical("FILE NOT FOUND: " + csv_full_path)
        return
    
    if exists(cached_csv_full_path): 
        dfCached = pd.read_csv(cached_csv_full_path)
        dfCached.set_index(SCHEMA_ATTRIBUTE_COMPANY_ID, inplace=True, drop=False)
    else:
        log.warning("No Cached file found. First time running?")

    dfNew = pd.read_csv(csv_full_path)
    #set the index of the dataframe. Lets us access the data easier by looking up via index
    dfNew.set_index(SCHEMA_ATTRIBUTE_COMPANY_ID, inplace=True, drop=False)

    #here is where the magic happens. We can concat two dataframes together to understand what changed
    #notice how we drop the duplicates
    diffs = pd.concat([dfCached,dfNew]).drop_duplicates(keep=False)
    log.info("There are %s differences between the last run and this run", len(diffs))
    
    if(len(diffs) == 0):
        log.info("No Changes to the file this run. Returning..")
        return stats

    #here is where we store the different operations that could occur
    #we still process these one more time to ensure they are valid profiles
    #see pending_creates, pending_updates, and pending_deletes below
    creates = []
    updates = []
    deletes = []

    
    for index, row in diffs.iterrows():
        #Get Creates
        if index in dfNew.index and index not in dfCached.index:
            #creates
            creates.append(dfNew.loc[index])
        elif index in dfNew.index and index in dfCached.index:
            #updates
            updates.append(dfNew.loc[index])
        elif index not in dfNew.index and index in dfCached.index:
            #deletes
            dfNew.loc[index]
        else:
            log.warning("Something file difference didnt match an create, update, or delete")
        
    pending_creates = []
    pending_updates = []
    pending_deletes = []

    for company in creates: 
        if isValidCompany(company):
            pending_creates.append(convertToSecZettaJSON(company, "company"))

    for company in updates: 
        if isValidCompany(company):
            pending_updates.append(convertToSecZettaJSON(company, "company"))
    
    for company in deletes: 
        if isValidCompany(company):
            pending_deletes.append(convertToSecZettaJSON(company, "company"))
    
    #At this point we have an array of objects that are in JSON format
    # we can just pass this thru to the '/profiles' endpoint to create/update/delete

    log.info("Pending Creates: %s", len(pending_creates))
    log.info("Pending Updates: %s", len(pending_updates))
    log.info("Pending Deletes: %s", len(pending_updates))

    stats["total_creates"] = len(pending_creates)
    stats["total_updates"] = len(pending_updates)
    stats["total_deletes"] = len(pending_deletes)

    if len(pending_creates) > 0:
        #start creating profiles
        batch_size = 50
        log.debug("Processing Creates in batchces of %s....", batch_size)
        
        #store the batches in an array called tmp
        tmp = []
        for i in range(0,len(pending_creates)):
            tmp.append(pending_creates[i])
            if i % batch_size == 0:
                log.debug("Sending API request for this create batch...%s",i)
                data = {}
                data["profiles"] = tmp
                response = sendAPIRequest("POST","/profiles", data)
                log.info("%s) Attempted to create %s profiles. Batch API Response: %s", i, len(tmp), response.status_code)
                tmp = []

        #after looping there could still be some left over. So check the size of tmp before moving on
        if len(tmp) > 0:
            log.debug("There was a few left. Make sure we dont forget about them...")
            data = {}
            data["profiles"] = tmp
            response = sendAPIRequest("POST","/profiles", data)
            log.info("Attempted to create %s profiles. Batch API Response: %s", len(tmp), response.status_code)
                

    return stats

def processPropertyFile(filename):

    stats = {
        "total_creates": 0,
        "total_updates": 0,
        "total_deletes": 0,
        "sucessful_creates": 0,
        "sucessful_updates": 0,
        "sucessful_deletes": 0,
        "job_ids": []
    }

    #grab the file paths for both the regular file and the cached file
    cached_csv_full_path = CACHED_FOLDER + "cached-" + filename
    csv_full_path = DATA_FOLDER + filename
    #dataframes just help process CSV data quickly
    dfCached = pd.DataFrame()
    dfNew = pd.DataFrame()

    if not exists(csv_full_path):
        log.critical("FILE NOT FOUND: " + csv_full_path)
        return
    
    if exists(cached_csv_full_path): 
        dfCached = pd.read_csv(cached_csv_full_path)
        dfCached.set_index(SCHEMA_ATTRIBUTE_PROPERTY_ID, inplace=True, drop=False)
    else:
        log.warning("No Cached file found. First time running?")

    dfNew = pd.read_csv(csv_full_path)
    dfNew.set_index(SCHEMA_ATTRIBUTE_PROPERTY_ID, inplace=True, drop=False)

    #here is where the magic happens. We can concat two dataframes together to understand what changed
    #notice how we drop the duplicates
    diffs = pd.concat([dfNew,dfCached]).drop_duplicates(keep=False)
    log.info("There are %s differences between the last run and this run", len(diffs))
    
    #here is where we store the different operations that could occur
    #we still process these one more time to ensure they are valid profiles
    #see pending_creates, pending_updates, and pending_deletes below
    creates = []
    updates = []
    deletes = []

    
    for index, row in diffs.iterrows():
        #Get Creates
        if index in dfNew.index and index not in dfCached.index:
            #creates
            creates.append(dfNew.loc[index])
        elif index in dfNew.index and index in dfCached.index:
            #updates
            updates.append(dfNew.loc[index])
        elif index not in dfNew.index and index in dfCached.index:
            #deletes
            deletes.append(dfCached.loc[index])
        else:
            log.warning("Something file difference didnt match an create, update, or delete")
        
    pending_creates = []
    pending_updates = []
    pending_deletes = []

    for property in creates: 
        if isValidProperty(property):
            pending_creates.append(convertToSecZettaJSON(property, "property"))

    for property in updates: 
            if isValidProperty(property):
                pending_updates.append(convertToSecZettaJSON(property, "property"))

    for property in updates: 
            if isValidProperty(property):
                pending_deletes.append(convertToSecZettaJSON(property, "property"))


    #At this point we have an array of objects that are in JSON format
    # we can just pass this thru to the '/profiles' endpoint to create/update/delete

    log.info("Pending Creates: %s", len(pending_creates))
    log.info("Pending Updates: %s", len(pending_updates))
    log.info("Pending Deletes: %s", len(pending_updates))

    stats["total_creates"] = len(pending_creates)
    stats["total_updates"] = len(pending_updates)
    stats["total_deletes"] = len(pending_deletes)

    if len(pending_creates) > 0:
        #start creating profiles
        batch_size = 50
        log.debug("Processing Creates in batchces of %s....", batch_size)
        
        #store the batches in an array called tmp
        tmp = []
        for i in range(0,len(pending_creates)):
            tmp.append(pending_creates[i])
            if i % batch_size == 0:
                log.debug("Sending API request for this create batch...%s",i)
                data = {}
                data["profiles"] = tmp
                response = sendAPIRequest("POST","/profiles", data)
                log.info("%s) Attempted to create %s profiles. Batch API Response: %s", i, len(tmp), response.status_code)
                tmp = []

        #after looping there could still be some left over. So check the size of tmp before moving on
        if len(tmp) > 0:
            log.debug("There was a few left. Make sure we dont forget about them...")
            data = {}
            data["profiles"] = tmp
            response = sendAPIRequest("POST","/profiles", data)
            log.info("Create: %s", response.status_code)

    return stats


#########################################################################################################
# Name: is Valid Company
# Parameters:
#   company_df: this is a pandas dataframe that contains the company data
#               you can access individual elements by calling company_df["attribute_name"]
# Purpose: 
#   Will return true/false whenever this company has all of the required data elements
#########################################################################################################
def isValidCompany(company_df):
    #error checking first off
    if (SCHEMA_ATTRIBUTE_COMPANY_NAME not in company_df or
        SCHEMA_ATTRIBUTE_STATUS not in company_df or
        SCHEMA_ATTRIBUTE_PRIMARY_COMPANY_CODE not in company_df or
        SCHEMA_ATTRIBUTE_SECONDARY_COMPANY_CODE not in company_df or
        SCHEMA_ATTRIBUTE_ACCOUNT_TYPE not in company_df or
        SCHEMA_ATTRIBUTE_NALO_INTL not in company_df or
        SCHEMA_ATTRIBUTE_REGION not in company_df):
        log.error("Required Attributes dont exist for company. Failing!")
        exit()

    name = company_df[SCHEMA_ATTRIBUTE_COMPANY_NAME]

    if company_df[SCHEMA_ATTRIBUTE_STATUS] != "Active":
        log.debug("Disregarding Company %s because its status was %s", name, company_df[SCHEMA_ATTRIBUTE_STATUS])
        return False

    if pd.isnull(company_df[SCHEMA_ATTRIBUTE_PRIMARY_COMPANY_CODE]):
        log.debug("Disregarding Company %s because its primary code wasn't popluated", name)
        return False


    return True

#########################################################################################################
# Name: Is Valid Property
# Parameters:
#   property_df: this is a pandas dataframe that contains the property data
#               you can access individual elements by calling property_df["attribute_name"]
# Purpose: 
#   Will return true/false whenever this company has all of the required data elements
#########################################################################################################
def isValidProperty(property_df):

    #error checking first off
    if (SCHEMA_ATTRIBUTE_PROPERTY_ID not in property_df or
        SCHEMA_ATTRIBUTE_PROPERTY_STATUS not in property_df or
        SCHEMA_ATTRIBUTE_PROPERTY_NAME not in property_df):
        log.error("Required Attributes dont exist for property. Failing!")
        exit()

    name = property_df[SCHEMA_ATTRIBUTE_PROPERTY_NAME]
    status = property_df[SCHEMA_ATTRIBUTE_PROPERTY_STATUS]
    division = property_df[SCHEMA_ATTRIBUTE_PROPERTY_LVL1_DIVISION]
    unit = property_df[SCHEMA_ATTRIBUTE_PROPERTY_LVL1_UNIT]
    department = property_df[SCHEMA_ATTRIBUTE_PROPERTY_LVL1_DEPARTMENT]
    log.info("Checking Property: %s to see if its valid",name)

    if not (status == "Open" or  status == "Pre-Opening"):
        log.debug("Disregarding Property %s because its status was %s", name, status)
        return False

    if pd.isnull(division) or pd.isnull(unit) or pd.isnull(department):
        log.debug("Disregarding %s Property %s because DUD wasnt complete %s : %s : %s", status, name, division, unit, department)
        return True

    log.debug("Property %s is a valid property.", name)
    return True


#########################################################################################################
# Name: Convert To SecZetta JSON
# Parameters:
#   company_df: this is a pandas dataframe that contains the company data
# Purpose: 
#   Will a dictionary of the new company profile JSON. This translates the file attributes to the 
#   actual SecZetta attributes that are required to create the profile
#########################################################################################################
def convertToSecZettaJSON(df, type):

    if type.lower() == "company":
        dict = df.to_dict()
        delete = []
        for att in dict:
            if pd.isna(dict[att]):
                delete.append(att)

        for att in delete:
            del dict[att]

        new_sz_dict = {}
        for att in dict:
            new_sz_dict[SCHEMA_CONVERSION_DICT[att]] = dict[att]


        json = {
            "profile_type_id": PROFILE_TYPE_ID_COMPANIES,
            "status": 1,
            "attributes": new_sz_dict
        }
        return json
    if type.lower() == "property":
        dict = df.to_dict()
        delete = []
        for att in dict:
            if pd.isna(dict[att]):
                delete.append(att)

        for att in delete:
            del dict[att]

        new_sz_dict = {}
        for att in dict:
            if (att == SCHEMA_ATTRIBUTE_PROPERTY_MANAGEMENT_COMPANY or
                att == SCHEMA_ATTRIBUTE_PROPERTY_OWNER_COMPANY or 
                att == SCHEMA_ATTRIBUTE_PROPERTY_FRANCHISEE_COMPANY or 
                att == SCHEMA_ATTRIBUTE_PROPERTY_ASSET_MANAGEMENT_COMPANY):
                new_sz_dict[SCHEMA_CONVERSION_DICT[att]] = getCompanyId(dict[att])
            else:
                new_sz_dict[SCHEMA_CONVERSION_DICT[att]] = dict[att]


        json = {
            "profile_type_id": PROFILE_TYPE_ID_PROPERTIES,
            "status": 1,
            "attributes": new_sz_dict
        }
        return json

#########################################################################################################
# Name: Get Company ID
# Purpose: 
#   Will store company_id in a cached dictionary. key/value of company_account_id/seczetta_profile_id
#########################################################################################################
def getCompanyId(company_account_id):
    global COMPANY_CACHE, COMPANY_CACHE_LOADED

    if COMPANY_CACHE_LOADED == False:
        log.info("Company Cache isn't loaded. Loading....")
        if not exists(COMPANY_CACHE_FILE_PATH):
            log.warning("No Cache File Exists at %s. Creating Blank one.", COMPANY_CACHE_FILE_PATH)
            f = open(COMPANY_CACHE_FILE_PATH, "w")
            f.write("acct_id,sz_id")
            f.close()
        else:
            with open(COMPANY_CACHE_FILE_PATH) as cache_file:
                csv_reader = csv.reader(cache_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        account_id = row[0]
                        sz_id = row[1]
                        COMPANY_CACHE[account_id] = sz_id
                        line_count += 1
                log.info("Company Cache Loaded! %s company ids were loaded.", line_count-1)
        COMPANY_CACHE_LOADED = True

    if company_account_id in COMPANY_CACHE:
        sz_id = COMPANY_CACHE[company_account_id]
        if sz_id == "":
            return None 
        else:
            return sz_id
    else:
        log.info("Didn't have Company with ID: %s in cache. Gotta grab it from the system!", company_account_id)       
        company = {}
        data = {
            "advanced_search": {
                "condition_rules_attributes": [
                    {
                        "type": "ProfileTypeRule",
                        "comparison_operator": "==",
                        "value": PROFILE_TYPE_ID_COMPANIES
                    },
                    {
                        "type": "ProfileAttributeRule",
                        "condition_object_id": ATTRIBUTE_ID_COMPANY_ACCOUNT_ID,
                        "object_type": "NeAttribute",
                        "comparison_operator": "==",
                        "value": company_account_id
                    }
                ]
            }
        }

        response = sendAPIRequest("POST","/advanced_search/run",data)
        if response.status_code == 200:
            log.debug("200 OK. Grabbed New Company ID for %s", company_account_id)
            json = response.json()
            if "profiles" in json:
                profiles = json["profiles"]
                
                if len(profiles) > 1:
                    log.warning("Profiles Length wasn't 1. Do we have duplicate companies?")
                elif len(profiles) < 1:
                    log.warning("company with account_id %s not found in SecZetta", company_account_id)
                    cacheCompanyIds(company_account_id, "")
                    return None
                else:
                    company = profiles[0]
                    company_profile_id = company["id"]
                    COMPANY_CACHE[company_account_id] = company_profile_id
                    cacheCompanyIds(company_account_id, company_profile_id)
                    return company_profile_id
        else:
            log.error("API Failed. Status Code: %s. Message: %s", response.status_code, response.json())

def cacheCompanyIds(account_id, sz_id):
    f = open(COMPANY_CACHE_FILE_PATH, "a")
    f.write("\n"+account_id +","+sz_id)
    f.close()

#company_stats = processCompanyFile("POC-Companies.csv")
#property_stats = processPropertyFile("POC-Properties.csv")
