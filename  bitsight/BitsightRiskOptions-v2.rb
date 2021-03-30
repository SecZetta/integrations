require 'net/http'
require 'uri'
require 'json'
require 'pp'
require 'OpenSSL'

$NE_TOKEN = 'f8b38fd1df2a4fbb98db03a93c468644'
$NEP_URL = 'https://taylordemo.mynonemployee.com/api/'

## Builds a JSON Array of Options ##
def populate_attr_options(attr_id, start_num, end_num, request_type)
	options_hash = { 'ne_attribute_options' => Array.new }
	for num in start_num..end_num
		opt = {
			'ne_attribute_id' => attr_id,
			'option' => (num / 10.0).to_s #,
			# 'order' => num
		}
		options_hash['ne_attribute_options'] << opt
	end

	json = JSON.generate(options_hash)
	make_API_request('ne_attribute_options',request_type,json)
end
##
## Make API Request ##
def make_API_request(uri_end, request_type, json_body = '')
    uri = URI.parse("#{$NEP_URL}#{uri_end}")
	request_type.downcase!
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
	request["Accept"] = "application/json"
    request["Authorization"] = "Token token=#{$NE_TOKEN}" 

	request.body = json_body unless json_body == ''

	req_options = {
		use_ssl: uri.scheme == "https",
		verify_mode: OpenSSL::SSL::VERIFY_NONE
	}

	response = Net::HTTP.start(uri.hostname, uri.port, req_options) { |http| http.request(request) }

	# if is_nep
	# 	puts "NE API #{request_type} code: #{response.code}"
	# 	puts "NE API #{request_type} response:"

	# 	if request_type != 'get' then pp JSON.parse(response.body) end
	# end
    response
end
##
populate_attr_options("db5e2aa7-c414-475d-b2cc-43835e9df712",0,99,'create')