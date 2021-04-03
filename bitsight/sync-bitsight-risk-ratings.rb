require 'net/http'
require 'uri'
require 'json'
require 'pp'
require 'OpenSSL'
require 'Date'

# Your SecZetta API Key
$NE_TOKEN = 'c6bda210f92142188032f5a7b59ed0f6'
# Your BitSight Token
$BS_TOKEN = 'd24b46958ece37895493f3811422569a61196760'
# Your SecZetta Tenant URL
$NEP_URL = 'https://idproofdemo.nonemployee.com/api/'
# Profile Type ID for your Vendors
VENDOR_ID = "37826aa2-ada3-4077-82ac-e90b4a8ce910"

## Populate Hash for NEtP Vendors
def build_vendors_hash(vendors_raw)
	hash_map = Hash.new

	vendors_raw.each do |vendor|
		if(vendor['attributes']['bitsight_guid'] != nil)
	    	hash_map[vendor['attributes']['bitsight_guid']] = vendor
		end
	end
	hash_map
end
##

## Make API Request ##
def make_API_request(uri_end, request_type, json_body = '', is_nep = true, auth = {type: 'token', token: $NE_TOKEN})
	if is_nep then uri = URI.parse("#{$NEP_URL}#{uri_end}")
    else uri = URI.parse(uri_end) end
	case request_type
		when 'get'
			request = Net::HTTP::Get.new(uri)
		when 'create'
			request = Net::HTTP::Post.new(uri)
		when 'update'
            request = Net::HTTP::Patch.new(uri)
        when 'delete'
            request = Net::HTTP::Delete.new(uri)
		else request = ''
	end

	request.content_type = "application/json"

    if auth[:type] == 'token' then request["Authorization"] = "Token token=#{auth[:token]}" end
    if auth[:type] == 'basic' then request.basic_auth auth[:username], auth[:password] end

	request["Accept"] = "application/json"
	request.body = json_body unless json_body == ''

	req_options = {
		use_ssl: uri.scheme == "https",
		verify_mode: OpenSSL::SSL::VERIFY_NONE
	}

	response = Net::HTTP.start(uri.hostname, uri.port, req_options) { |http| http.request(request) }

	if is_nep
		puts "NE API #{request_type} code: #{response.code}"
		puts "NE API #{request_type} response:"

		if request_type != 'get' then pp JSON.parse(response.body) end
	end
    response
end
##
## Get BitSight Companies API Request
def get_bs_companies(vendors)
    response = make_API_request("https://api.bitsighttech.com/ratings/v1/companies",'get','',false,{type: 'basic', username: $BS_TOKEN, password: ''})
	companies = JSON.parse(response.body)['companies']

	puts "BitSight API code: #{response.code}, #{companies.length} companies sent"
	if response.code != "200"
		puts "BitSight API response:"
		pp JSON.parse(response.body)
	end

	creates = updates = Array.new
	companies.each do |company|
		current_vendor = vendors[company['guid']]
		if(current_vendor != nil)
			if(current_vendor['attributes']['bitsight_rating_date']==company['rating_date']) then next end
			profile = build_profile_hash(company, current_vendor['id'])
			updates << profile
		else
			profile = build_profile_hash(company)
			creates << profile
		end
	end
	lists = {
		creates: creates,
		updates: updates,
	}
end
##
## Build Profile Hash From BS Company
def build_profile_hash(co, id=nil)
	profile = Hash.new
	if (id != nil) then profile['id'] = id
	else profile['status'] = 1 end

	profile['name'] = co['name']
    profile['profile_type_id'] = VENDOR_ID
	profile['attributes'] = {
		'vendor_name' => co['name'],
        'bitsight_inherited_security_rating' => scale_unit(co['rating'],250,900,10,0,true).round(1).to_s,
        'bitsight_rating' => co['rating'].to_s,
        'bitsight_rating_date' => Date.parse(co['rating_date']).strftime('%m/%d/%Y'),
        'bitsight_guid' => co['guid'],
        'bitsight_full_vendor_risk_assessment_complete' => 'No'
		}
	profile
end
##
## Converts a number from one scale to another
def scale_unit(n, start1, stop1, start2, stop2, limit = false)
    norm = (n - start1) / (stop1 - start1).to_f
    norm = norm.clamp(0,1) if limit
	((norm * (stop2 - start2)) + start2)
end
##
## Breaks the API requests into chunks of 100
def bulk_APIrequests(uri_end, request_type, hash_arr)
	if(hash_arr.length>0) then
		hash_arr.each_slice(99) do |x|
			json = JSON.generate({uri_end => x})
			#puts json
			res = make_API_request(uri_end,request_type,json)
		end
	else puts "No data for #{request_type.capitalize} in array" end
end
##

# Gets a hashmap full of vendor objects from SecZetta
vendors = build_vendors_hash(JSON.parse(make_API_request("profiles?profile_type_id=#{VENDOR_ID.to_s}",'get').body)['profiles'])

# Builds the lists of creates/updates that are required to Sync the BitSight data
lists = get_bs_companies(vendors)

# Uncomment the below to print out the rating --> scaled rating
#lists[:creates].each do | test |
#	puts test["attributes"]["bitsight_rating"] + "|==>|" + scale_unit(test["attributes"]["bitsight_rating"].to_f,250,900,0,10,true).round(1).to_s
#end

# Sends off the API requests to update/create the Vendor objects in SecZetta
bulk_APIrequests('profiles','update', lists[:updates])
bulk_APIrequests('profiles','create', lists[:creates])
