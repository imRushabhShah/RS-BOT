from wit import Wit
from pprint import pprint

access_token="accessToken" #confidential
client=Wit(access_token=access_token)

def witfunc(message):
    resp=client.message(message)
    entities=[]
    for key in resp['entities']:
        value=resp['entities'][key][0]['value']
        #print("key is",key,"the value is",value)
        entities.append((key,value))

    return(entities)


