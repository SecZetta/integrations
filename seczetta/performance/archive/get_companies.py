import multiprocessing as mp
import requests
import logging as log
import math

log.basicConfig(level=log.INFO)

API_BASE = "https://marriottperformancedev.nonemployee.com/api"
API_KEY = "18bae8c5f1944a71a502721ba460b18d"
LIMIT = 40

def sendAPIRequest(verb, url, data):
    log.debug("Entering sendAPIRequest %s %s", verb, url)

    verb = verb.upper()
    url = API_BASE + url

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token='+API_KEY,
        'Accept': 'application/json'
    }

    log.debug("New URL: " + url)

    response = ""
    if(verb == "GET"):
        response = requests.get(url, headers=headers, json =data)

    if(verb == "POST"):
        response = requests.post(url, headers=headers, json = data)

    if(verb == "PATCH"):
        response = requests.patch(url, headers=headers, json = data)


    if response.status_code == 200:
        return response
    else:
        log.error("Error occured with API call: %s", response.status_code)

def get_companies(offset):
    new_offset = offset * LIMIT
    log.info("Starting %s) Executing Get Companies. Limit: %s Offset: %s",offset,LIMIT,new_offset)
    url = "/profiles?profile_type_id=57ad1a76-9bbe-48d3-825e-4a967ab3f372&&query[limit]="+str(LIMIT)+"&query[offset]=" + str(new_offset)
    response = sendAPIRequest("GET",url,{})
    log.info("Finishing %s) Executing Get Companies. Limit: %s Offset: %s",offset,LIMIT,new_offset)
    
    if response.status_code == 200:
        return response.json()["profiles"]
    else:
        log.error("Error Occurred.. Failing... %s", response.status_code)
        return []

if __name__ == "__main__":
    response = sendAPIRequest("GET", "/profiles?profile_type_id=57ad1a76-9bbe-48d3-825e-4a967ab3f372&&query[limit]=1&query[offset]=0&metadata=true", {})
    json = response.json()
    metadata = json["_metadata"]
    total_companies = metadata['total']

    total_offsets = math.ceil(total_companies / LIMIT)
    log.info("There are %s total companies. Which means at a limit of %s there will be %s total calls", total_companies, LIMIT, total_offsets)
    
    p = mp.Pool(processes=20)

    data = p.map(get_companies, [i for i in range(total_offsets)])
    p.close()

    profiles = []
    total = 0
    for arr in data:
        total += len(arr)
        profiles += arr

    company_dict = {}
    for p in profiles:
        print(p["name"])
        company_dict[p["attributes"]["company_account_id"]] = p["id"]
    
    print(len(company_dict))
