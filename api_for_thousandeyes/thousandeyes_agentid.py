import requests
class get_agentid:
    def __init__(self):
        self.username = 'noreply@thousandeyes.com'
        self.authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'
    @property
    def get_the_data(self):
        self.response = requests.get('https://api.thousandeyes.com/v6/agents.json', auth=(self.username, self.authtoken))
        self.json_response = self.response.json()['agents']
        self.new_data = []
        for self.numbers in self.json_response:
            if 'errorDetails' not in self.numbers:
                self.new_data.append({'agentId':self.numbers['agentId'],'agentName':self.numbers['agentName']})
        return self.new_data