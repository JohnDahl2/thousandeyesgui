import requests
import numpy as np
class thousand_API:
    def __init__(self):
        self.username = 'noreply@thousandeyes.com'
        self.authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'
    @property
    def get_the_data_agentId(self):
        pop = []
        response = np.array(requests.get('https://api.thousandeyes.com/v6/agents.json', auth=(self.username, self.authtoken)).json()['agents'])
        for index in range(len(response)):
            if 'errorDetails' not in response[index]:
                if ',' not in response[index]['agentName']:
                    response[index]['agentName'] = f"{response[index]['agentName']}, {response[index]['agentName']}"
                response[index]['agentState'] = response[index]['agentName'][response[index]['agentName'].find(',') + 2:]
            else:
                pop.append(index)
        response = np.delete(response, pop)
        return sorted(sorted(response, key =lambda city: city['agentState']), key = lambda city: len(city['agentState']))
    @property
    def get_the_data_testId(self):
        return np.array(requests.get('https://api.thousandeyes.com/v6/tests.json', auth=(self.username, self.authtoken)).json()['test'])