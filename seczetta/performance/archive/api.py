
API_BASE = 'https://taylordemo.mynonemployee.com/api'
DEBUG = False

def get_users():
    url = API_BASE + '/users'
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url

def get_profile_types():
    url = API_BASE + '/profile_types'
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url

def get_profiles_by_profile_type(profileTypeId):
    url = API_BASE + '/profiles?profile_type_id='+str(profileTypeId)
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url

def get_users_by_id(id):
    url = API_BASE + '/users/' + str(id)
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url

def create_profile():
    url = API_BASE + '/profile'
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url

def update_profile(id):
    url = API_BASE + '/profiles/' + id
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url

def advanced_search():
    url = API_BASE + '/advanced_search/run'
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url

def get_users():
    url = API_BASE + '/users'
    if DEBUG: print( '[DEBUG] Returning Url: ' + url)
    return url