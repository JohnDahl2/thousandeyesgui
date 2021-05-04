'''
This scirpt retreives the data from thousandeyes for the
jsons for the agentId and testId
'''
import requests
import numpy as np
class thousand_api:
    def __init__(self):
        self.username = 'noreply@thousandeyes.com'
        self.authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'
    @property
    def agentId(self):
        return np.array(list((filter(lambda x : x if 'errorDetails' not in x else '',np.array(requests.get('https://api.thousandeyes.com/v6/agents.json',
                auth=(self.username, self.authtoken)).json()['agents'])))))
    @property
    def testId(self):
        return np.array(requests.get('https://api.thousandeyes.com/v6/tests.json',
                auth=(self.username, self.authtoken)).json()['test'])
