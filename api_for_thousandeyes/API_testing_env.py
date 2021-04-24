import requests
import numpy as np
username = 'noreply@thousandeyes.com'
authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'

def get_the_data(u,a):
    response = requests.get('https://api.thousandeyes.com/v6/agents.json', auth=(u,a))
    json_response = response.json()['agents']
    new_data = []
    for numbers in json_response:
        if 'errorDetails' not in numbers:
            new_data.append({'agentId': numbers['agentId'], 'agentName': numbers['agentName']})
    return 'finished'

def get_the_data_pop(u,a):
    response = requests.get('https://api.thousandeyes.com/v6/agents.json', auth=(u, a))
    json_response = response.json()['agents']
    return 'finished'