import requests
class get_testid:
    def __init__(self):
        self.username = 'noreply@thousandeyes.com'
        self.authtoken = 'g351mw5xqhvkmh1vq6zfm51c62wyzib2'
    @property
    def get_the_data(self):
        self.response = requests.get('https://api.thousandeyes.com/v6/tests.json', auth=(self.username, self.authtoken))
        self.json_response = self.response.json()['test']
        self.new_data = []
        for self.numbers in self.json_response:
            self.new_data.append({'testId':self.numbers['testId'],'testName':self.numbers['testName'],'type':self.numbers['type']})
        return self.new_data