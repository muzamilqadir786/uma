def getClientData(url, retries=5, sleepTimeout=5):
    for i in xrange(retries):
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11")]
            response = opener.open(url)
            return response.read()
        except:
            time.sleep(sleepTimeout)
 
    return None
#opener.addheaders = [("Content-Type","application/json"),("Accept", "application/json"),("Host", "https://hostname"),("Authorization", "Bearer")]
getClientData('')

import urllib, urllib2
import json
import time
import requests

"""

Registers Client to Gluu server using OpenID connect

"""

def RegisterClient(url, retries=5, sleepTimeout=5):
    headers = {"Content-Type": "application/json",
                "Accept": "application/json"
                "Host": "server.example.com"
                "Authorization": "Bearer"
    }
    
    data = {
        "application_type": "web",
        "redirect_uris":
             ["https://client.example.org/callback",
              "https://client.example.org/callback2"],
        "client_name": "My Example",
        "token_endpoint_auth_method": "client_secret_basic",
        "jwks_uri": "https://client.example.org/my_public_keys.jwks",
        "userinfo_encrypted_response_alg": "RSA1_5",
        "userinfo_encrypted_response_enc": "A128CBC-HS256",
        "contacts": ["ve7jtb@example.org", "mary@example.org"],
        "request_uris":
         ["https://client.example.org/rf.txt"]
      }
    
    for i in xrange(retries):
        try:            
            response = requests.post(url,payload=headers,data=data)            
            response = response.read()
            return response.read()
        except:
            time.sleep(sleepTimeout)

    return None

#Gluu Server Register URL
register_url = '/connect/register'

json_data = json.reads(RegisterClient(register_url))

if not json_data.has_key("error"):
    client_id = json_data['client_id']
    client_secret = json_data['client_secret']
    registration_access_token =  json_data['registration_access_token']
    registration_client_uri = json_data['registration_client_uri']
    """
    Saving client id and secret to json file
    
    """"
    
    client = {}
    client["client_id"] = client_id
    client["client_secret"] = client_secret
    client["registeration_access_token"] = registeration_access_token
    client["registeration_client_uri"] = registeration_client_uri
    
    with open("credentials.json","wb") as credentials_file:
        credentials = json.dumps(client)
        credentials_file.write(credentials)
        print credentials
        
else:
    print json_data["error_description"]

def clientReadRequest():
    return requests.get(registeration_client_uri)


    

def callAPI(url):
    response = requests.get(api_url)
    if response.status == 403:
        ticket = getPermissionTicket()
        RPT_token = getRPT(client_id,client_secret,ticket)

    
        
        
def getPermissionTicket():
    ticket =

def getRPT(client_id,client_secret,ticket):
    data = {"client_id":client_id, "client_secret":client_secret, "ticket": ticket}
    url = '' #Gluu server uri to return RPT token
    return requests.post(url, data)

def getBearerToken():
    
    





            
    
