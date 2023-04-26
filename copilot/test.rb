# write a function that makes a post request to a url and returns the json response

require 'net/http'
require 'json'

def post_request(url, params)
  uri = URI(url)
  res = Net::HTTP.post_form(uri, params)
  JSON.parse(res.body)
end

