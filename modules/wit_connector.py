from wit import Wit
import requests

def wit_connection(auth_token):
    """
    This function connect to Wit.ai api.
    """
    return Wit(auth_token)

def wit_attributes(auth_token):
    """
    This function gets the attributes from Wit.ai api and return a dictionary with entities and traits.
    """

    v = '20200728'
    hed = {'Authorization': 'Bearer ' + auth_token}
    url = 'https://api.wit.ai/'
    
    attributes = {
        'entities': requests.get(url + 'entities?v={}'.format(v), headers=hed),
        'traits': requests.get(url + 'traits?v={}'.format(v), headers=hed)
    }
    # Return the attributes from server
    return attributes
