import requests
class get_agentid:
    def __init__(self):
        self.username = 'noreply@thousandeyes.com'
        self.authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'
    @property
    def get_the_data(self):
        response = requests.get('https://api.thousandeyes.com/v6/agents.json', auth=(self.username, self.authtoken))
        json_response = response.json()['agents']
        new_data = []
        for numbers in json_response:
            if 'errorDetails' not in numbers:
                new_data.append({'agentId':numbers['agentId'],'agentName':numbers['agentName']})
        return new_data
    @property
    def reformat_agent_id(self):
        current_data = self.get_the_data
        for index in range(len(current_data)):
            current_row = current_data[index]
            if ',' not in current_row['agentName']:
                current_row['agentName'] = f"{current_row['agentName']}, {current_row['agentName']}"
            current_data[index]['agentState'] = current_row['agentName'][current_row['agentName'].find(',') + 2:]
        return sorted(sorted(current_data, key =lambda city: city['agentState']), key = lambda city: len(city['agentState']))