import requests
import json

def getCreds() :
	""" Get creds required for use in the applications

	Returns:
		dictonary: credentials needed globally
	"""

	creds = dict() # dictionary to hold everything
	creds['access_token'] = 'EAAE1DOnsY6IBANKBqn0ZAyQFPPU7Af8zT40FumCN4RoeetyUpM6B2a23tO9fzAPCooR9QwGFhqZCQepytZCI4yHlllseQNYSlCns7hNYDxGHP6638osF9DKHUZBjrgTJwfOEKiHr3D8Q5VZCu21RXpJHHl7VTKqcZD' # access token for use with all api calls
	creds['client_id'] = '339804557173666' # client id from facebook app IG Graph API Test
	creds['client_secret'] = '5250b56dddd6689b6a6820b0ea590e6d' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = 'v8.0' # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = 'no' # debug mode for api call
	creds['page_id'] = '152377118263715' # users page id
	creds['instagram_account_id'] = '17841402298349642' # users instagram account id
	creds['ig_username'] = 'by_kiara' # ig username

	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :
	""" Request data from endpoint with params

	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters
	Returns:
		object: data from the endpoint
	"""

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print ("\nURL: ") # title
	print (response['url']) # display url hit
	print ("\nEndpoint Params: ") # title
	print (response['endpoint_params_pretty']) # display params passed to the endpoint
	print ("\nResponse: ") # title
	print (response['json_data_pretty']) # make look pretty for cli
