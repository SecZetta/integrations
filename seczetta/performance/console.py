import os
from os import path
import json
from csv import reader
import requests
import uuid
import api
import random
api.DEBUG = False
        


VERSION = 1.0
ENVIRONMENT = None
API_KEY = None
BASE_URL = None
PROFILE_TYPES = {}
ENVIRONMENTS = {}
OBJECTS = []
PROFILE_STATUSES = {
    "Active": 1,
    "Inactive": 2,
    "Leave of absence": 3,
    "Terminated": 4
}


def startConsole():
    global ENVIRONMENT, ENVIRONMENTS, OBJECTS
    #clear the terminal of any extra text
    os.system('cls' if os.name == 'nt' else 'clear')

    #load the config file initially
    f = open('config.json',) 
    data = json.load(f) 
    for e in data['config']['environments']: 
        ENVIRONMENTS[e["name"]] = e
    for o in data['config']['objects']:
        OBJECTS.append(o)
    f.close() 

    #print out welcome splash screen
    welcomeStr = "==== SecZetta API Console v" + str(VERSION) + " ==="
    lineStr = ""
    for i in range(len(welcomeStr)):
        lineStr += "="
    print(lineStr)
    print(welcomeStr)
    print(lineStr)

    #Grab the environment selection from the user
    environment(["e"]) #calling it with the command



    while getInput() == False:   
         v=1
    print("\nGoodbye!")

def getInput():
    global ENVIRONMENT
    inputStr = "> "
    print("\nEnter a command (type ? for help)")
    if(ENVIRONMENT != None):
        inputStr = ENVIRONMENT +"> "
    strInput = input(inputStr)
    arrInput = strInput.split(" ")
    cmd = arrInput[0]
    return executeCommand(cmd,arrInput)

def executeCommand(cmd, array):
    if cmd == "test":
        test()
        return False
    if cmd == "help" or cmd == "h" or cmd == "?": 
        help()
        return False
    elif cmd == "clear" or cmd == "cls": 
        clear()
        return False
    elif cmd == "e" or "environment".startswith(cmd) : 
        environment(array)
        return False
    elif cmd == "export" or "export".startswith(cmd.lower()):
        export(array)
        return False
    elif cmd == "import" or "import".startswith(cmd.lower()):
        importCSV(array)
        return False
    elif "status".startswith(cmd) : 
        status()
        return False
    elif cmd.lower() == "json":
        parseJson(array)
        return False
    elif cmd.lower() == "uid":
        printUUID()
        return False
    elif "get".startswith(cmd) and "profiletypes".startswith(array[1].lower()): 
        getProfileTypes()
        return False
    elif "get".startswith(cmd) and "profiles".startswith(array[1].lower()): 
        getProfiles()
        return False
    elif cmd == "exit" or cmd == "quit" or cmd == "q":
        return True #exit
    elif "contributors".startswith(cmd):
        setContributors()
        return False
    else:
        notfound()
        return False
def test():
    global PROFILE_TYPES,OBJECTS
    print(OBJECTS)
    return
    index = 0
    for pt in PROFILE_TYPES:
        index += 1
        print(str(index)+") " + pt)
    pt = input(": ")
    print(list(PROFILE_TYPES.keys())[int(pt)-1])

def help():
    print("environment [environment_name] - sets the environment variables")
    print("  example: env taylordemo")
    print("clear - clears the terminal")
    print("status - gets current status of console")
    print("export profile [filename.csv] - grabs the profile of a certain type and exports it to a file")
    print("import [filename.csv] - imports the given csv and creates/updates profiles")
    print("getProfileTypes - gets the current environments profile types")
    print("json - parses json file **in progess**")
    print("uid - generates a unique UUID and UID")
    print("quit - quits the console")

def environment(array):
    global ENVIRONMENT
    #loadEnvironment([""])
    if(len(array) == 1):
        ENVIRONMENT = None
        while ENVIRONMENT is None: 
            print('Choose your environment:')
            selection = 0
            for e in ENVIRONMENTS:
                selection += 1
                print(str(selection) + ") " + e)

            envSelect = input("Which environment (1): ")
            if envSelect == "":
                envSelect = 1
            try:
                env = ENVIRONMENTS[list(ENVIRONMENTS.keys())[int(envSelect)-1]]
                envName = env["name"]
                loadEnvironment(envName)
            except ValueError:
                print("ERROR: Invalid Selection. Try Again")
                continue
    elif(len(array) == 2):
        loadEnvironment(array[1])

def loadEnvironment(env):
    global ENVIRONMENTS, ENVIRONMENT, API_KEY, BASE_URL


    if env in ENVIRONMENTS:
        ENVIRONMENT = ENVIRONMENTS[env]["name"]
        API_KEY = ENVIRONMENTS[env]["apiKey"]
        BASE_URL = ENVIRONMENTS[env]["url"]
        api.API_BASE = BASE_URL
        getProfileTypes(False)
        print("Success! " + env + " has been loaded")
    else:
        print("ERROR: No Environment named " + env + " was found")
    
def status():
    print("ENVIRONMENT: " + str(ENVIRONMENT))
    print("API_KEY: " + str(API_KEY))
    print("BASE_URL: " + str(BASE_URL))

def notfound():
    print("Command Not Found. Try Again.")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getProfileTypes(showValues = True):
    global ENVIRONMENT, PROFILE_TYPES
    PROFILE_TYPES = {}
    if(ENVIRONMENT == None):
        print("ERROR: No Environment Selected!")
        return
    
    x = sendAPIRequest("GET", api.get_profile_types(), {})
    jsonResponse = x.json()
    if(showValues): print("\n Profile Types ["+str(len(jsonResponse['profile_types']))+"]")
    row = 0
    for pt in jsonResponse['profile_types']:
        row += 1
        if(showValues):
            print(" " + str(row) + ") " + pt["name"])
            print("    > ID:       " + pt["id"])
            print("    > UID:      " + pt["uid"])
            print("    > NAME:     " + pt["name"])
            print("    > ARCHIVED: " + str(pt["archived"]))
        PROFILE_TYPES[pt["name"]] = pt["id"]
        
def getProfiles():
    global ENVIRONMENT
    if(ENVIRONMENT == None):
        print("ERROR: No Environment Selected!")
        return
    global API_KEY
    global BASE_URL

    
    profileTypeId = input(ENVIRONMENT +"> Enter the ProfileType ID: ")

    body = {
        "advanced_search": {
            "label": "Get Profiles of Type",
            "condition_rules_attributes": [
                {
                    "type": "ProfileTypeRule",
                    "comparison_operator": "==",
                    "value": profileTypeId
                }
            ]
        }
    }

    url = BASE_URL+"/advanced_search/run"
    print(body)
    x = requests.get(url, headers=headers, data = json.dumps(body))
    print(url)

    print(x.status_code)
    response = x.json()
    print(response)
    print("\n Profiles ["+str(len(response['profiles']))+"]")
    row = 0
    for p in response['profiles']:
        row += 1
        print(" " + str(row) + ") " + p["name"])
        print("    > ID:          " + p["id"])
        print("    > UID:         " + p["uid"])
        print("    > NAME:        " + p["name"])
        print("    > PType ID:    " + p["profile_type_id"])
        print("    > STATUS:      " + p["status"])
        print("    > ID PROOFING: " + p["id_proofing_status"])

def export(arr):
    global ENVIRONMENT, PROFILE_TYPES, OBJECTS
    numRows = 0
    tempDataFile = "temp-"
    for i in range(0,10):
        tempDataFile += str(random.randint(0,9))
    tempDataFile += ".json"
    if(len(arr) != 3):
        print("ERROR: Invalid Command Syntax. Please use export [object] [filename]")
        return
    
    obj = arr[1].lower()
    validObject = False
    for o in OBJECTS:
        if(obj.lower() == o.lower()):
            validObject = True
            obj = o
            break

    if validObject == False:
        print("ERROR: Object Type [" + str(obj) + "] was not found." )
        return

    fileName = arr[2]

    if(ENVIRONMENT == None):
        print("ERROR: No Environment Selected!")
        return

    if obj.lower() == "profiles":
        global PROFILE_TYPES
        populatedAttributes = ["id", "uid", "name", "profile_type_id", "status"]
        printProfileTypes()
        pt = input("What Profile Type: ")
        profileTypeId = str(PROFILE_TYPES[list(PROFILE_TYPES.keys())[int(pt)-1]])
        done = False
        loops = 0
        limit = 100
        offset = 0
        temp = open(tempDataFile, "w")
        temp.write("{ \"profiles\": [")
        numRows = 0
        while(done == False):
            loops += 1
            response = sendAPIRequest("GET",api.get_profiles_by_profile_type(profileTypeId) + "&query[limit]="+str(limit)+"&query[offset]="+str(offset),{})
            responseJSON = response.json()
            if "error" in responseJSON:
                print("Finished Fetching Profiles. A total of " + str(numRows) + " were found.")
                done = True
                break
            for p in responseJSON['profiles']:
                numRows += 1
                if numRows != 1:
                    temp.write(",")
                json.dump(p,temp)
            
            print("Fetching more profiles. " + str(numRows) + " profiles fetched.")
            offset += limit
        temp.write("]}")
        temp.close()
        with open(tempDataFile) as f:
            data = json.load(f)
            for p in data['profiles']:
                if("id_proofing_status" in p and "id_proofing_status" not in populatedAttributes):
                    populatedAttributes.append("id_proofing_status")
                if("attributes" in p):
                    #has additional attributes
                    for att in p["attributes"]:
                        if att in populatedAttributes:
                            continue
                        populatedAttributes.append(att)
            #ok, we have all the attributes that had a value, now time to put them into a csv
            f = open(fileName, "w")
            #write the header first
            line = ""
            for att in populatedAttributes:
                line = line + att + ","
            line = line[:-1]
            f.write(line + "\n")
            line = ""
            for p in data['profiles']:
                for att in populatedAttributes:
                    if(att in p):
                        line = line + "\"" + str(p[att]) + "\","
                    elif(att in p["attributes"]):
                        line = line + "\"" + str(p["attributes"][att]) + "\","
                    else:
                        line = line + "\"\","
                line = line[:-1]
                f.write(line + "\n")
                line = ""
            

        f.close()
        os.remove(tempDataFile)
        
    if obj.lower() == "profiletypes":
        populatedAttributes = ["id", "uid", "name", "archived"]
        done = False
        numRows = 0
        response = sendAPIRequest("GET",api.get_profile_types(),{})
        responseJSON = response.json()
        f = open(fileName, "w")
        #write the header first
        line = ""
        for att in populatedAttributes:
            line = line + att + ","
        line = line[:-1]
        f.write(line + "\n")
        line = ""
        for p in responseJSON['profile_types']:
            numRows+=1
            for att in populatedAttributes:
                if(att in p):
                    line = line + "\"" + str(p[att]) + "\","
                else:
                    line = line + "\"\","
            line = line[:-1]
            f.write(line + "\n")
            line = ""
        f.close()
        #os.remove(tempDataFile)
    
    if obj.lower() == "users":
        populatedAttributes = ["id", "uid", "type", "name", "email", "title", "status", "login"] 
        done = False
        numRows = 0
        getUsersUrl = api.get_users() + "?query[limit]=250&query[offset]=0"
        response = sendAPIRequest("GET",getUsersUrl,{})
        responseJSON = response.json()
        f = open(fileName, "w")
        #write the header first
        line = ""
        for att in populatedAttributes:
            line = line + att + ","
        line = line[:-1]
        f.write(line + "\n")
        line = ""
        for p in responseJSON['users']:
            numRows+=1
            for att in populatedAttributes:
                if(att in p):
                    line = line + "\"" + str(p[att]) + "\","
                else:
                    line = line + "\"\","
            line = line[:-1]
            f.write(line + "\n")
            line = ""
        f.close()
    print("Success! Exported "+ str(numRows) +" "+obj+" to " + str(fileName))

def importCSV(arr):
    global PROFILE_TYPES, PROFILE_STATUSES
    #right now it just does profiles
    required = ["profile_type_id", "status"]
    
    if len(arr) != 2:
        print("ERROR: Invalid Syntax: import [filename].csv")
        return
    
    fileName = arr[1]
    if path.exists(fileName) == False:
        print("ERROR: File named "+str(fileName)+" not found.")
        return

    printProfileTypes()
    pt = input("What Profile Type: ")
    profileTypeId = str(PROFILE_TYPES[list(PROFILE_TYPES.keys())[int(pt)-1]])

    numRows = 0
    # open file in read mode
    successfulImports = 0
    error = False
    with open(fileName, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        header = []
        profiles = []
        for row in reader(read_obj):
            numRows+=1
            if(numRows == 1):
                print(row)
                if row[0] != "id" :
                    print("ERROR: Invalid File Format. ID should be the first attribute in the header")
                    return
                for att in row:
                    header.append(att)
                continue
            col = 0
            createProfile = True
            profile = {}
            for att in row:
                profile[header[col]] = att
                col+=1
            profiles.append(profile)
            
        #first loop thru and just set some of the 'special' attributes. I know this isnt very perfomrant..
        ops = { "CREATE": 0, "UPDATE": 0}
        for p in profiles:
            if "profile_type_id" not in p or p["profile_type_id"] == "":
                p["profile_type_id"] = profileTypeId
            if "status" not in p or p["status"] == "":
                p["status"] = 1
            if "id" not in p or p["id"] == "":
                p["op"] = "CREATE"
                ops["CREATE"] += 1
            else:
                p["op"] = "UPDATE"
                ops["UPDATE"] += 1
            
            if p["status"]:
                try:
                    status = int(p["status"])
                    p["status"] = status
                except:
                    status = PROFILE_STATUSES[p["status"]]
                    p["status"] = status

        
        print("Profiles to be imported: " + str(len(profiles)) + " profiles.")
        print("  Creates: " + str(ops["CREATE"]))
        print("  Updates: " + str(ops["UPDATE"]))

        check = input("Are you sure you want to continue? (Y):")
        if check == "":
            check = "Y"
        check = check.lower()
        if check != "y":
            print("Import Cancelled.")
            return
    
        requestBody = {}
        for p in profiles: 
            profileBody = {}
            attributesBody = {}
            for att in p:
                if att == "id" or att == "op" or att == "status" or att == "profile_type_id" or att == "name" or att == "uid":
                    continue
                if p[att].startswith("[") and p[att].endswith("]"):
                    #found array, converting
                    strVal = p[att][1:-1]
                    arr = strVal.split(",")
                    attributesBody[att] = arr
                else:
                    attributesBody[att] = p[att]

            profileBody["profile_type_id"] = p["profile_type_id"]       
            profileBody["status"] = p["status"]       
            profileBody["attributes"] = attributesBody  
            requestBody["profile"] = profileBody     
            x = {}
            
            if(p["op"] == "UPDATE"):
                x = sendAPIRequest("PATCH",api.update_profile(p["id"]), requestBody)
                rJson = x.json()
                if x.status_code == 200:
                    successfulImports += 1
                    try:
                        print("200 OK: " + rJson["profile"]['name'] + " was updated successfully!")
                    except:
                        print("200 OK: " + rJson["profile"]['id'] + " was updated successfully!")
                else:
                    print("ERROR Occurred!")
                    print(str(x.status_code) + ": " + str(rJson))
                    print(requestBody)
                    error = True
                    break
            else:
                x = sendAPIRequest("POST",api.create_profile(), requestBody)
                rJson = x.json()
                if x.status_code == 201:
                    successfulImports+=1
                    try:
                        print("201 Created: " + rJson["profile"]['name'] + " was created successfully!")
                    except:
                        print("201 Created: " + rJson["profile"]['id'] + " was created successfully!")
                else:
                    print("ERROR Occurred!")
                    print(str(x.status_code) + ": " + str(rJson))
                    print(requestBody)
                    error = True
                    break
    if error:
        print("ERROR Occurred. " + str(successfulImports) + " out of " + str(len(profiles)) + " were successfully updated. ")
        print("\n\nError Occurred on ROW #" + str(successfulImports + 2) + "\n\n")
    else:    
        print("Import Successful! " + str(successfulImports) + " out of " + str(len(profiles)) + " profiles were updated.")

def printUUID():
    print("Here is your unique UUID and UID if required:")
    print("UUID:", str(uuid.uuid4()) )
    print("UID: ", str(uuid.uuid4()).replace("-","") )

def parseJson(arr):
    if len(arr) != 2:
        print("ERROR: Invalid Syntax: json [filename].json")
        return
    
    fileName = arr[1]
    if path.exists(fileName) == False:
        print("ERROR: File named "+str(fileName)+" not found.")
        return

    attributesThatRequireUpdate = ['workflow_id', 'step_id', 'id', 'uid']
    unneededClasses = [
        'ProfileType',
        'ProfilePage'
    ]

    with open(fileName) as f:
        data = json.load(f)
        classNames = {}
        wfObjs = []
        idDict = {}
        for p in data:
            className = p['class_name']
            if className not in classNames:
                classNames[className] = 1
            else:
                classNames[className] += 1
            # if "UpdateWorkflow" == className:
            #     workflowID = str(uuid.uuid4())
            #     workflowUID = uuid.uuid4().hex
            #     idDict[p['id']] = workflowID
            #     idDict[p['uid']] = workflowUID
            #     p['id'] = workflowID
            #     p['uid'] = workflowUID
            #     p['name'] = p['name'] + ' copy'
            #     wfObjs.append(p)
            # else:
            #     if 'uid' in p:
            #         idDict[p['uid']] = uuid.uuid4().hex
            #     for att in attributesThatRequireUpdate:
            #         if att in p:
            #             if p[att] not in idDict:
            #                 idDict[p[att]] = str(uuid.uuid4())
            #             p[att] = idDict[p[att]]

            # if "WorkflowStep" == className or "action" in className.lower():
            #     wfObjs.append(p)
        
        #print(json.dumps(wfObjs))
        i = 1    
        for c in classNames:
            print(i, ")", c)
            i = i + 1
        

#### HELPERS ####
def sendAPIRequest(verb, url, data):

    verb = verb.upper()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token='+API_KEY,
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
    
def printProfileTypes():
    global PROFILE_TYPES
    index = 0
    for pt in PROFILE_TYPES:
        index += 1
        print(str(index)+") " + pt)


def setContributors():

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
        

startConsole()

