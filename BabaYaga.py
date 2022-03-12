import math
import json
import random
import requests

class Curse(object):
	email = ""
	proxy = ""
	headers = ""
	payload = ""
	url = ""
	user = ""
	firstName = ""
	lastName = ""
	
def prepare(fN, lN, mP, Px, Nl, uA):
	curse = Curse()
	curse.email = fN+"."+lN+"@"+mP
	curse.proxy = Px
	curse.headers = Nl['headers']
	curse.payload = Nl['payload']
	curse.user = uA
	curse.firstName = fN
	curse.lastName = lN
	if 'scheme' in curse.headers:
		curse.url = curse.headers['scheme'] + '://' + curse.headers[':authority'] +	curse.headers[':path']
	elif 'Host' in curse.headers:
		curse.url = "https://" + curse.headers['Host']
		
	return curse

def cast(c):
	print("Invoking \""+c.url+"\" for a curse on \""+c.email+"\"! (via \""+c.proxy+"\" emulating \""+c.user+"\")")
	
	# Session initiation
	session = requests.Session()
	session.mount('https://', requests.adapters.HTTPAdapter())
	print(str(session))
	payload = c.payload
	if 'email' in payload:
		try:
			payload['email'] = c.email
			print(str(payload))
		except KeyError:
			print("KeyError: invalid JSON key for email address (key=email)")
	elif 'email_address' in payload:
		try:
			payload['email_address'] = c.email
			print(str(payload))
		except KeyError:
			print("KeyError: invalid JSON key for email address (key=email_address)")
	
	headers = c.headers
	headers['User-Agent'] = c.user
	headers['content-length'] = str(len(json.dumps(payload)))
	print(str(headers))
	
	#Proxy setup
#	https_proxy = c.proxy
#	session.proxies = {
#		'http' : https_proxy,
#		'https' : https_proxy
#	}
#	print(https_proxy)
	
	data = payload
	
	# POST
	try:
		print("attempting post request")
		x = session.post(c.url, data, headers)
		print(x.status_code)
	except:
		print("Unknown Error")
	
	print("Spellcast successful.")
	